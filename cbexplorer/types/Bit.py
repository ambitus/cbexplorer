#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from .AbstractType import AbstractType


class Bit(AbstractType):
    length = None

    def __init__(self, locator, length, bit_mask=None):
        self.locator = locator
        self.length = length
        self.bit_mask = bit_mask

    def __call__(self, control_block=None):
        chunk = int.from_bytes(self._get_chunk(), byteorder="big")
        if self.bit_mask:
            masked_chunk = chunk & self.bit_mask

            return bool(masked_chunk)
        else:
            return bool(chunk)
