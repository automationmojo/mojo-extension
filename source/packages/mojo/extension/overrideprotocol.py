"""
.. module:: overrideprotocol
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the `OverrideProtocol` declaration.

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

from typing import Dict, Protocol

from mojo.extension.overridepack import OverridePack

class OverrideProtocol(Protocol):

    def get_override_pack() -> OverridePack:
        ...
