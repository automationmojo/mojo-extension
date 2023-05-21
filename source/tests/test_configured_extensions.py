
from typing import Type

import sys
import unittest

from mojo.extension.extensionconfiguration import ExtensionConfiguration
from mojo.extension.wellknown import ConfiguredSuperFactorySingleton

from myextinst import MyExtInstProtocol, MyExtInstFactory
from myexttype import MyExtTypeProtocol, MyExtTypeFactory


class TestConfiguredExtensions(unittest.TestCase):

    def setUp(self) -> None:
        ExtensionConfiguration.CONFIGURED_FACTORY_MODULES = [
            "myextinst",
            "myexttype"
        ]

        self._super_factory = ConfiguredSuperFactorySingleton()
        return super().setUp()
    
    def test_create_instance_by_order(self):

        hey = self._super_factory.create_instance_by_order(MyExtInstProtocol.give_me_a_hey, 1, 2, 3, A="A", B="B", C="C")
        ho = self._super_factory.create_instance_by_order(MyExtInstProtocol.give_me_a_ho, 1, 2, 3, A="A", B="B", C="C")

        print("")
        print(f"{hey}... {ho}... {hey}... {ho}...")

        return
    
    def test_create_instance_for_each(self):

        output = ""

        for i in range(2):
            for hey in self._super_factory.create_instance_for_each(MyExtInstProtocol.give_me_a_hey, 1, 2, 3, A="A", B="B", C="C"):
                output += f"{hey}... "
                for ho in self._super_factory.create_instance_for_each(MyExtInstProtocol.give_me_a_ho, 1, 2, 3, A="A", B="B", C="C"):
                    output += f"{ho}... "

        print("")
        print(output)

        return
    
    def test_get_override_types_by_order(self):

        hey_type = self._super_factory.get_override_types_by_order(MyExtTypeProtocol.give_me_a_hey)
        ho_type = self._super_factory.get_override_types_by_order(MyExtTypeProtocol.give_me_a_ho)

        hey = hey_type()
        ho = ho_type()

        print("")
        print(f"{hey}... {ho}... {hey}... {ho}...")

        return
    
    def test_interate_override_types_for_each(self):

        output = ""

        for i in range(2):
            for hey_type in self._super_factory.iterate_override_types_for_each(MyExtTypeProtocol.give_me_a_hey):
                output += f"{hey_type()}... "
                for ho_type in self._super_factory.iterate_override_types_for_each(MyExtTypeProtocol.give_me_a_ho):
                    output += f"{ho_type()}... "

        print("")
        print(output)

        return

if __name__ == '__main__':
    unittest.main()