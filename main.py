#!/usr/bin/env python3.10

from loguru import logger
from model import Analog, Digital


def main():
    # valve_1 = Analog()
    # logger.debug(valve_1)
    # #
    # # valve_1.get_signal(100)
    # # logger.debug(valve_1)
    # # #
    # # # valve_1.get_signal(-100)
    # # # logger.debug(valve_1)
    # # # #
    # # valve_1.get_signal(0)
    # # logger.debug(valve_1)
    # # #
    # valve_1.get_signal('-100')
    # logger.debug(valve_1)

    valve_2 = Digital()
    logger.debug(valve_2)

    valve_2.get_signal(131)
    logger.debug(valve_2)
    #
    # valve_2.get_signal(False)
    # logger.debug(valve_2)


if __name__ == '__main__':
    main()
