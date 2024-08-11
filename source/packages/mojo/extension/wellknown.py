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

from mojo.errors.exceptions import SemanticError

from mojo.collections.singletons import SINGLETON_LOCK

from mojo.startup.presencevariables import MOJO_PRESENCE_VARIABLES

from mojo.extension.superfactory import SuperFactory

def ConfiguredSuperFactorySingleton():

    global CONFIGURED_SUPER_FACTORY

    SINGLETON_LOCK.acquire()
    try:
        if CONFIGURED_SUPER_FACTORY is None:
            extension_modules = []

            if MOJO_PRESENCE_VARIABLES.MJR_EXTENSION_MODULES is None:
                errmsg = "You must first call 'resolve_presence_variables' before attempting to create a SuperFactory singleton."
                raise SemanticError(errmsg)

            extension_modules_value: str = MOJO_PRESENCE_VARIABLES.MJR_EXTENSION_MODULES
            extension_modules_value.strip()

            if len(extension_modules_value) > 0:
                extension_modules = extension_modules_value.split(",")
            
            CONFIGURED_SUPER_FACTORY = SuperFactory(extension_modules)
    finally:
        SINGLETON_LOCK.release()

    return CONFIGURED_SUPER_FACTORY

