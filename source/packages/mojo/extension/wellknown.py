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


CONFIGURED_SUPER_FACTORY = None

from mojo.extension.extensionvariables import MOJO_EXTENSION_VARIABLES
from mojo.extension.superfactory import SuperFactory

def ConfiguredSuperFactorySingleton():

    global CONFIGURED_SUPER_FACTORY

    if CONFIGURED_SUPER_FACTORY is None:
        factory_modules = []

        factory_modules_value = MOJO_EXTENSION_VARIABLES.MJR_CONFIGURED_FACTORY_MODULES.strip()
        if len(factory_modules_value) > 0:
            factory_modules = factory_modules_value.split(",")
        
        CONFIGURED_SUPER_FACTORY = SuperFactory(factory_modules)

    return CONFIGURED_SUPER_FACTORY

