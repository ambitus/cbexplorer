#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from .Locator import Locator


class FileLocator(Locator):
    def __init__(self, base_location):
        self._file_descriptor = base_location
        self._offset = 0

    def new_from(self, offset):
        new_self = FileLocator(self._file_descriptor)
        new_self._offset = offset + self._offset
        return new_self

    def content(self, size):
        self._file_descriptor.seek(self._offset)
        content = self._file_descriptor.read(size)
        return content
