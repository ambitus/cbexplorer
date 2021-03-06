#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from .AddressLocator import AddressLocator
from .FileLocator import FileLocator


class LocatorFactory:
    LOCATORS = {
        "address": lambda x: AddressLocator(x),
        "file": lambda x: FileLocator(x),
    }

    @staticmethod
    def create(name, base_location):
        if name in LocatorFactory.LOCATORS.keys():
            return LocatorFactory.LOCATORS[name](base_location)
        else:
            raise ValueError(f"{name} locator not found.")
