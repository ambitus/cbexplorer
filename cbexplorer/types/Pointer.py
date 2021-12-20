#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from .AbstractType import AbstractType


class Pointer(AbstractType):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, control_block=None):
        address = int.from_bytes(self._get_chunk(), byteorder="big", signed=False)
        if control_block:
            return control_block(self.locator.new_from(address))
        else:
            return address


class Pointer8(Pointer):
    length = 1


class Pointer15(Pointer):
    length = 2


class Pointer16(Pointer):
    length = 2


class Pointer24(Pointer):
    length = 3


class Pointer31(Pointer):
    length = 4


class Pointer32(Pointer):
    length = 4


class Pointer64(Pointer):
    length = 8
