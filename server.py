import logging
import asyncio

from asyncua import ua, Server
from config import URL, URL_IDX
from asyncua.common.type_dictionary_builder import DataTypeDictionaryBuilder


async def main():
    server = Server()
    await server.init()
    server.set_endpoint(URL)
    server.set_server_name('OPC server ')

    # idx name will be used later for creating the xml used in data type dictionary
    idx = await server.register_namespace(URL_IDX)

    dict_builder = DataTypeDictionaryBuilder(server, idx, URL_IDX, 'MyDictionary')
    await dict_builder.init()

    valve_struct_name = 'ValveName'
    valve_struct = await dict_builder.create_data_type(valve_struct_name)
    valve_struct.add_field('State',  ua.VariantType.String)
    valve_struct.add_field('Signal',  ua.VariantType.String)

    machine_struct_name = 'FactoryName'
    machine_struct = await dict_builder.create_data_type(machine_struct_name)
    # machine_struct.add_field('Name', ua.VariantType.String)

    machine_struct.add_field('NameMachine', valve_struct, is_array=True)

    await dict_builder.set_dict_byte_string()

    await server.load_type_definitions()

    valve_var = await server.nodes.objects.add_variable(
        idx,
        'Valve',
        None,
        datatype=valve_struct.data_type
    )

    await valve_var.set_writable()
    var = ua.ValveName()
    var.State = 'None'      # Подпихнуть переменную
    var.Signal = 'None'     # Подпихнуть переменную
    await valve_var.write_value(var)

    machine_var = await server.nodes.objects.add_variable(
        idx,
        'Machine',
        None,
        datatype=machine_struct.data_type
    )

    await machine_var.set_writable()
    var2 = ua.FactoryName()
    var2.NameMachine = [var, var]
    # var2.Name = 'Machine #1'
    await machine_var.write_value(var2)

    async with server:
        print(getattr(dict_builder, '_type_dictionary').get_dict_value())

        v1 = await valve_var.read_value()
        v2 = await machine_var.read_value()

        while True:
            await asyncio.sleep(1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(
                main()
            )
