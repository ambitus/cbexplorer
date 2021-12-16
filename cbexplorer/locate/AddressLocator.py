#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from ctypes import string_at

from .Locator import Locator


class AddressLocator(Locator):
    def __init__(self, base_location):
        self._address = base_location

    @staticmethod
    def _memory_read(address, size):
        return string_at(address, size)

    def new_from(self, offset):
        new_self = AddressLocator(self._address + offset)
        return new_self

    def content(self, size):
        return AddressLocator._memory_read(self._address, size)
