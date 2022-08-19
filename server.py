#!/usr/bin/env python3.10
import asyncio
from model import Analog, Digital
from asyncua import ua, Server
from config import URL, URL_IDX
from asyncua.common.type_dictionary_builder import DataTypeDictionaryBuilder

async def server():

    valve_analog_1 = Analog(state='Open')
    valve_digital_2 = Digital(state='Close')

    server = Server()
    await server.init()
    server.set_endpoint(URL)
    server.set_server_name('OPC server ')

    # idx name will be used later for creating the xml used in data type dictionary
    idx = await server.register_namespace(URL_IDX)

    dict_builder = DataTypeDictionaryBuilder(server, idx, URL_IDX, 'MyDictionary')
    await dict_builder.init()

    valve_struct_name = 'Valve'
    valve_struct = await dict_builder.create_data_type(valve_struct_name)
    valve_struct.add_field('Type', ua.VariantType.String)
    valve_struct.add_field('State', ua.VariantType.String)
    valve_struct.add_field('Signal', ua.VariantType.String)

    machine_struct_name = 'FactoryName'
    machine_struct = await dict_builder.create_data_type(machine_struct_name)
    # machine_struct.add_field('Name', ua.VariantType.String)
    machine_struct.add_field('NameMachine', valve_struct, is_array=True)

    await dict_builder.set_dict_byte_string()

    await server.load_type_definitions()

    var1 = ua.Valve()
    var1.Type = str('Analog')
    var1.State = str(valve_analog_1.state)
    var1.Signal = str(valve_analog_1.signal)

    var2 = ua.Valve()
    var2.Type = str('Digital')
    var2.State = str(valve_digital_2.state)
    var2.Signal = str(valve_digital_2.signal)

    machine_var = await server.nodes.objects.add_variable(
        idx,
        'Factory',
        None,
        datatype=machine_struct.data_type
    )

    await machine_var.set_writable()
    var3 = ua.FactoryName()
    var3.NameMachine = [var1, var2]
    # var2.Name = 'Machine #1'
    await machine_var.write_value(var3)

    async with server:
        print(getattr(dict_builder, '_type_dictionary').get_dict_value())

        v1 = await machine_var.read_value()

        while True:
            await asyncio.sleep(1)
