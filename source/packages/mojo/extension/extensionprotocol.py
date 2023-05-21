
from typing import Protocol

class ExtProtocol(Protocol):

    ext_protocol_name = None

    def __init_subclass__(cls, *args, **kwargs):
        if cls.ext_protocol_name is None:
            errmsg = "The 'protocol_name' class level fiedl must be set on derived protocol types."
            raise RuntimeError(errmsg)
        return super().__init_subclass__(*args, **kwargs)
        