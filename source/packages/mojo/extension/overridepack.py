
from typing import Dict

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
