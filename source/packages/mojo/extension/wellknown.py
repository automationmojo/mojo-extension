"""
.. module:: wellknown
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the :class:`ConfiguredSuperFactorySingleton` function
               which provides a singleton instance of the SuperFactory type.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

CONFIGURED_SUPER_FACTORY = None

from mojo.extension.extensionvariables import ExtensionConfiguration
from mojo.extension.superfactory import SuperFactory

def ConfiguredSuperFactorySingleton():

    global CONFIGURED_SUPER_FACTORY

    if CONFIGURED_SUPER_FACTORY is None:
        factory_modules = ExtensionConfiguration.MJR_CONFIGURED_FACTORY_MODULES
        CONFIGURED_SUPER_FACTORY = SuperFactory(factory_modules)

    return CONFIGURED_SUPER_FACTORY

