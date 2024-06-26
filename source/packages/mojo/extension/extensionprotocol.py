
"""
.. module:: extensionprotocol
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the ExtProtocol base type.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []


from typing import Protocol

class ExtProtocol(Protocol):

    ext_protocol_name = None

    def __init_subclass__(cls, *args, **kwargs):
        if cls.ext_protocol_name is None:
            errmsg = "The 'protocol_name' class level fiedl must be set on derived protocol types."
            raise RuntimeError(errmsg)
        return super().__init_subclass__(*args, **kwargs)
        