"""
.. module:: extensionsettings
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the extension settings and defaults.

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

from typing import Optional

import os

from mojo.startup.startupconfigloader import StartupConfigLoader
from mojo.startup.converters import CSV_TO_UNIQUE_LIST_CONVERTER

scloader = StartupConfigLoader("MOJO-EXTENSION")


class MOJO_EXTENSION_VARIABLE_DEFAULTS:


    MJR_NAME = scloader.get_variable_value("MJR_NAME", default="mjr")

    MJR_HOME_DIRECTORY = scloader.get_variable_value("MJR_HOME_DIRECTORY",
            default=os.path.expanduser(os.path.join("~", MJR_NAME)))
    MJR_HOME_DIRECTORY = os.path.abspath(os.path.expandvars(os.path.expanduser(MJR_HOME_DIRECTORY)))

    MJR_CONFIGURED_FACTORY_MODULES = scloader.get_variable_value(
        "MJR_CONFIGURED_FACTORY_MODULES", default=[], converter=CSV_TO_UNIQUE_LIST_CONVERTER
    )

EXTENSION_SETTINGS_ESTABLISHED = False

def establish_extension_settings(name: Optional[str]=None, home_dir: Optional[str]=None):
    """
        The `establish_extension_settings` method is called to modify the name and home folder of the
        environment.  This is accomplished by overloading a the 'Startup' defaults.  The name and home
        directory might still be changed later during the 'Parameterize' phase.

        :param name: A one word name for the environment.
        :param home_directory: The home directory where configuration files and results will be stored.
    """
    global EXTENSION_SETTINGS_ESTABLISHED

    if not EXTENSION_SETTINGS_ESTABLISHED:
        EXTENSION_SETTINGS_ESTABLISHED = True
        if name is not None:
            MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_NAME = name
        if home_dir is not None:
            MOJO_EXTENSION_VARIABLE_DEFAULTS.MJR_HOME_DIRECTORY = home_dir

    return
