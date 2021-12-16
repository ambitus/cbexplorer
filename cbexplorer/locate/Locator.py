#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
