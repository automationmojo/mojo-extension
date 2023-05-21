

from typing import Type

from mojo.extension.extensionfactory import ExtFactory
from mojo.extension.extensionprotocol import ExtProtocol


class Hey:
    def __str__(self):
        return "Hey"

class Ho:
    def __str__(self):
        return "Ho"


class MyExtTypeProtocol(ExtProtocol):

    ext_protocol_name = "mojo-myextypeprotocol"

    @classmethod
    def give_me_a_hey(cls) -> Type[Hey]:
        ...
    
    @classmethod
    def give_me_a_ho(cls) -> Type[Ho]:
        ...

class MyExtTypeFactory(ExtFactory, MyExtTypeProtocol):

    @classmethod
    def give_me_a_hey(cls) -> Hey:
        return Hey
    
    @classmethod
    def give_me_a_ho(cls) -> Ho:
        return Ho
