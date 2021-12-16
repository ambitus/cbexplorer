import unittest
import tempfile
from unittest.mock import patch

from cbexplorer.locate import LocatorFactory
from cbexplorer.locate.AddressLocator import AddressLocator
from cbexplorer.locate.FileLocator import FileLocator

class LocatorFactoryTest(unittest.TestCase):
    def test_factory_with_default_locators(self):
        addressLocator = LocatorFactory.create("address", 0)
        fileLocator = LocatorFactory.create("file", 0)

        self.assertIsInstance(addressLocator, AddressLocator)
        self.assertIsInstance(fileLocator, FileLocator)

    def test_factory_with_wrong_locator(self):
        with self.assertRaises(ValueError):
            LocatorFactory.create('something', 0)

class AddressLocatorTest(unittest.TestCase):
    memory = "0123456789abcdefghijklmnopqrstuvwxzy"

    def setUp(self):
        self.locator = LocatorFactory.create("address", 0)

    def test_new_from(self):
        new_locator = self.locator.new_from(10)
        self.assertEqual(new_locator._address, 10)

    @patch("cbexplorer.locate.AddressLocator.AddressLocator._memory_read", lambda x, y: AddressLocatorTest.memory[x:x+y])
    def test_content(self):
        self.assertEqual(self.locator.content(10), "0123456789")

class FileLocatorTest(unittest.TestCase):
    file_content = "0123456789abcdefghijklmnopqrstuvwxzy"

    def setUp(self):
        self.file_descriptor = tempfile.TemporaryFile(mode="w+")
        self.file_descriptor.write(FileLocatorTest.file_content)
        self.locator = LocatorFactory.create("file", self.file_descriptor)

    def test_new_locator(self):
        self.assertEqual(self.locator.content(4), "0123")
        self.assertEqual(self.locator.content(10), "0123456789")

    def test_new_with_locator(self):
        new_locator = self.locator.new_from(5)
        self.assertEqual(new_locator.content(5), "56789")
        self.assertEqual(new_locator.content(2), "56")
