

CONFIGURED_SUPER_FACTORY = None

from mojo.extension.extensionvariables import ExtensionConfiguration
from mojo.extension.superfactory import SuperFactory

def ConfiguredSuperFactorySingleton():

    global CONFIGURED_SUPER_FACTORY

    if CONFIGURED_SUPER_FACTORY is None:
        factory_modules = ExtensionConfiguration.MJR_CONFIGURED_FACTORY_MODULES
        CONFIGURED_SUPER_FACTORY = SuperFactory(factory_modules)

    return CONFIGURED_SUPER_FACTORY

