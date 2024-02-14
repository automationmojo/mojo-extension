"""
.. module:: overridevariables
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

from mojo.startup.startupconfigloader import StartupConfigLoader
from mojo.startup.converters import CSV_TO_UNIQUE_LIST_CONVERTER
from mojo.startup.startupvariables import MOJO_STARTUP_VARIABLES

scloader = StartupConfigLoader("MOJO-EXTENSION")

class MOJO_EXTENSION_VARIABLES(MOJO_STARTUP_VARIABLES):


    MJR_NAME = scloader.get_variable_value("MJR_NAME", default="mjr")


    MJR_HOME_DIRECTORY = scloader.get_variable_value("MJR_HOME_DIRECTORY",
            default=os.path.expanduser(os.path.join("~", MJR_NAME)))
    MJR_HOME_DIRECTORY = os.path.abspath(os.path.expandvars(os.path.expanduser(MJR_HOME_DIRECTORY)))


    # For the `MJR_CONFIGURED_FACTORY_MODULES` variable, if we find it in the environment,
    # then the value set in the environment.  If the value is not found in the environment,
    # then the loader will look in the `MOJO-EXTENSIONS` section of the startup config. If
    # the value is not found in either location, the specifieid default is used.

    MJR_CONFIGURED_FACTORY_MODULES = scloader.get_variable_value(
        "MJR_CONFIGURED_FACTORY_MODULES", default=[], converter=CSV_TO_UNIQUE_LIST_CONVERTER
    )


def establish_rebranded_home(name: str, home_directory: str):
    """
        The `establish_rebranded_home` method is called to modify the name and home folder of the
        environment.

        :param name: A one word name for the environment.
        :param home_directory: The home directory where configuration files and results will be stored.
    """
    MOJO_EXTENSION_VARIABLES.MJR_NAME = name
    MOJO_EXTENSION_VARIABLES.MJR_HOME_DIRECTORY = home_directory
    return