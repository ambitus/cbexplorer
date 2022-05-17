#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#
from cbexplorer.types import *
from cbexplorer.locate import Locator

class DummyLocator(Locator):

    def __init__(self):
        self.value = 0

    def new_from(self, offset):
        return self

    def content(self, size):
        return self.value

dl = DummyLocator()

def test_char_type():
    dl.value = 'AAAA'
    my_char = Char(dl, length=4)
    assert my_char() == 'AAAA'

def test_int_type():
    dl.value = (4).to_bytes(4, byteorder='big')
    my_int = Integer(dl)
    assert my_int() == 4


def test_bit_type():
    dl.value = (4).to_bytes(1, byteorder='big')
    my_true_bit = Bit(dl, 1, 4)
    assert my_true_bit() == True

    my_false_bit = Bit(dl, 1, 3)
    assert my_false_bit() == False

def test_pointer_type():
    dl.value = (1234).to_bytes(4, byteorder='big')
    my_pointer = Pointer31(dl)
    assert my_pointer() == 1234
