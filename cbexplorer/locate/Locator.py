#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from abc import ABC, abstractclassmethod


class Locator(ABC):
    @abstractclassmethod
    def __init__(self, base_location):
        pass

    @abstractclassmethod
    def new_from(self, offset):
        pass

    @abstractclassmethod
    def content(self, size):
        pass
