#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

from abc import ABC, abstractclassmethod


class AbstractControlBlock(ABC):
    @abstractclassmethod
    def dump_fields(self):
        pass

    def dump(self):
        field_string = f"{self.__class__.__name__}"
        for field in self.dump_fields():
            field_value = getattr(self, field)
            field_string = field_string + f"\n\t{field}: {field_value}"

        return field_string

    def dump_to_file(self, filename):
        with open(filename, "wb") as f:
            for field in self.dump_fields():
                field_value = getattr(self, field)
                if isinstance(field_value, bytes):
                    val = field_value
                elif isinstance(field_value, int):
                    val = field_value.to_bytes(4, "big")
                else:
                    val = bytearray(field_value)
                f.write(val)
