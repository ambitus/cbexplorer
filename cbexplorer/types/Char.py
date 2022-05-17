#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from .AbstractType import AbstractType


class Char(AbstractType):
    length = None

    def __init__(self, locator, length=0):
        self.locator = locator
        self.length = length

    def __call__(self):
        return self._get_chunk()
