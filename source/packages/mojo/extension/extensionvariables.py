"""
.. module:: extensionvariables
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the ExtensionConfiguration variables.

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

import os

from mojo.startup.startupvariables import MOJO_STARTUP_VARIABLES

from mojo.extension.extensionsettings import MOJO_EXTENSION_VARIABLE_DEFAULTS

from mojo.collections.wellknown import ContextSingleton
from mojo.collections.contextpaths import ContextPaths

class MOJO_EXTENSION_VARIABLES(MOJO_STARTUP_VARIABLES):


    MJR_NAME = MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_NAME
    MJR_HOME_DIRECTORY = MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_HOME_DIRECTORY


    # For the `MJR_CONFIGURED_FACTORY_MODULES` variable, if we find it in the environment,
    # then the value set in the environment.  If the value is not found in the environment,
    # then the loader will look in the `MOJO-EXTENSIONS` section of the startup config. If
    # the value is not found in either location, the specifieid default is used.

    MJR_CONFIGURED_FACTORY_MODULES = MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_CONFIGURED_FACTORY_MODULES


def resolve_extension_variables():
    """
        This method allows environment variables to be used to override configuration file and branding settings. This
        is useful for integration.
    """

    ctx = ContextSingleton()

    MOJO_EXTENSION_VARIABLES.MJR_NAME = MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_NAME
    if "MJR_NAME" in os.environ:
        MOJO_EXTENSION_VARIABLES.MJR_NAME = os.environ["MJR_NAME"]
    ctx.insert(ContextPaths.RUNTIME_NAME, MOJO_EXTENSION_VARIABLES.MJR_NAME)

    MOJO_EXTENSION_VARIABLES.MJR_HOME_DIRECTORY = MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_HOME_DIRECTORY
    if "MJR_HOME_DIRECTORY" in os.environ:
        MOJO_EXTENSION_VARIABLES.MJR_HOME_DIRECTORY = os.environ["MJR_HOME_DIRECTORY"]
    ctx.insert(ContextPaths.RUNTIME_HOME_DIRECTORY, MOJO_EXTENSION_VARIABLES.MJR_HOME_DIRECTORY)

    MOJO_EXTENSION_VARIABLES.MJR_CONFIGURED_FACTORY_MODULES = MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_CONFIGURED_FACTORY_MODULES
    if "MJR_CONFIGURED_FACTORY_MODULES" in os.environ:
        MOJO_EXTENSION_VARIABLES.MJR_CONFIGURED_FACTORY_MODULES = os.environ["MJR_CONFIGURED_FACTORY_MODULES"]
    ctx.insert(ContextPaths.RUNTIME_CONFIGURED_FACTORY_MODULES, MOJO_EXTENSION_VARIABLES.MJR_CONFIGURED_FACTORY_MODULES)

    return