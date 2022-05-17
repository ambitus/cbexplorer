#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#

"""
"""

from abc import ABC, abstractproperty, abstractmethod


class AbstractType(ABC):
    @abstractproperty
    def length(self):
        pass

    @abstractmethod
    def __call__(self):
        pass

    def _get_chunk(self):
        return self.locator.content(self.length)
