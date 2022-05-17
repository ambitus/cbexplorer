#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""


class Array:

    array_length = 0
    array_element_size = 0
    base_element = None

    def __init__(self, array_length, base_element, array_element_size):
        self.base_element = base_element
        self.array_length = array_length
        self.array_element_size = array_element_size

    def __call__(self):
        values = []
        # FIXME: do we need this?
        # data_size = self.base_element.length
        for i in range(self.array_length):
            values.append(self.base_element.__call__())
            self.base_element.locator = self.base_element.locator.new_from(
                self.array_element_size
            )

        return values
