
from typing import Type

from mojo.extension.extensionfactory import ExtFactory
from mojo.extension.extensionprotocol import ExtProtocol


class Hey:
    def __str__(self):
        return "Hey"

class Ho:
    def __str__(self):
        return "Ho"

class MyExtInstProtocol(ExtProtocol):

    ext_protocol_name = "mojo-myexinstprotocol"

    @classmethod
    def give_me_a_hey(cls) -> Hey:
        ...
    
    @classmethod
    def give_me_a_ho(cls) -> Ho:
        ...

class MyExtInstFactory(ExtFactory, MyExtInstProtocol):

    @classmethod
    def give_me_a_hey(cls, *args, **kwargs) -> Hey:
        return Hey()
    
    @classmethod
    def give_me_a_ho(cls, *args, **kwargs) -> Ho:
        return Ho()


