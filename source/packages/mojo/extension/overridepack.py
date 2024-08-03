"""
.. module:: overridepack
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the `OverridePack` dataclass.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []


from dataclasses import dataclass, asdict

@dataclass
class OverridePack:
    """
        An Overrideable class type is a class that has class-level variables
        that are intended to be overridden to modify package behavior.
    """

    @classmethod
    def override(cls, otable: "OverridePack"):

        for k, v in asdict(otable).items():
            if hasattr(cls, k):
                setattr(cls, k, v)

        return
