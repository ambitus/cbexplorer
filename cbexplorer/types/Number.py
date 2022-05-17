#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from .AbstractType import AbstractType


class Number(AbstractType):
    def __init__(self, locator, signed=True):
        self.locator = locator
        self.signed = signed

    def __call__(self):
        return int.from_bytes(self._get_chunk(), byteorder="big", signed=self.signed)


class Byte(Number):
    length = 1


class Short(Number):
    length = 2


class Integer(Number):
    length = 4


class Long(Number):
    length = 8
