#!/usr/bin/env python3.10

from loguru import logger
import logging
import asyncio
from server import server
from model import Analog, Digital


def get_valve():
    valve_analog_1 = Analog(state='Open')
    valve_analog_2 = Analog(state='Close')
    valve_digital_1 = Digital(state='Open')
    valve_digital_2 = Digital(state='Close')

    # logger.debug(valve_analog_1)
    # logger.debug(valve_analog_2)
    # logger.debug(valve_digital_1)
    # logger.debug(valve_digital_2)


def main():
    get_valve()


if __name__ == '__main__':
    main()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(server())
