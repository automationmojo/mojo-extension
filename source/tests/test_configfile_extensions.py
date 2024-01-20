
import tempfile
import unittest

from mojo.startup.startupvariables import MOJO_STARTUP_VARIABLES
from mojo.startup.wellknown import StartupConfigSingleton

from tests.myextinst import MyExtInstProtocol, MyExtInstFactory
from tests.myexttype import MyExtTypeProtocol, MyExtTypeFactory

CONFIG_CONTENT = """
[MOJO-EXTENSION]
MJR_CONFIGURED_FACTORY_MODULES = myextinst,myexttype
"""

class TestConfiguredExtensions(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        tempconfig = tempfile.mktemp()
        with open(tempconfig, 'w+') as cf:
            cf.write(CONFIG_CONTENT)

        MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS = tempconfig

        cls._startup_config = StartupConfigSingleton()
        cls._ext_config = cls._startup_config["MOJO-EXTENSION"]

        from mojo.extension.wellknown import ConfiguredSuperFactorySingleton
        cls._super_factory = ConfiguredSuperFactorySingleton()

        return
    
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