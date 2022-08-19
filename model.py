#!/usr/bin/env python3.10

from loguru import logger
from abc import ABC, abstractmethod


class Valve(ABC):
    """ Parental class of Valve """

    def __init__(self, state: str = None, signal: str | bool = None):
        """ Initial of Valve"""
        self.state = state
        self.signal = signal

    def __str__(self):
        return f'type = {self.__class__.__name__}, ' \
               f'state = {self.state}, ' \
               f'signal = {self.signal}'

    @abstractmethod
    def get_signal(self, signal: int | bool) -> int | bool | None:
        if signal is not None:
            return signal
        else:
            logger.info('signal is None')
            return None


class Analog(Valve):
    """Child class Analog Valve from Valve"""

    def __init__(self, **kwargs):
        """ Initial of Analog Valve"""
        super().__init__(**kwargs)

    @staticmethod
    def true_signal(signal: int) -> int | None:
        if isinstance(signal, int):
            return signal
            logger.debug(signal)
        else:
            return None
            logger.info('signal is not int')

    def get_signal(self, signal: int):
        if self.true_signal(signal) is not None:
            if 0 <= signal <= 100:
                self.signal = signal
                if signal == 0:
                    self.state = 'Close'
                else:
                    self.state = 'Open'
            else:
                self.state = self.state
                logger.info('signal out of range')


class Digital(Valve):
    """Child class Digital Valve from Valve"""

    def __init__(self, **kwargs):
        """ Initial of Digital Valve"""
        super().__init__(**kwargs)

    @staticmethod
    def true_signal(signal: bool) -> bool | None:
        if isinstance(signal, bool):
            return signal
            logger.debug(signal)
        else:
            return None
            logger.info('signal is not bool')

    def get_signal(self, signal: bool):
        if self.true_signal(signal) is not None:
            self.signal = signal
            if signal is True:
                self.state = 'Open'
            if signal is False:
                self.state = 'Close'
