
from typing import Dict, Protocol

from mojo.extension.overridepack import OverridePack

class OverrideProtocol(Protocol):

    def get_override_pack() -> OverridePack:
        ...
