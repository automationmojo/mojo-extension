
import importlib
import inspect
import logging
import sys

from types import ModuleType

from mojo.extension.extensionfactory import ExtFactory


logger = logging.getLogger()


def import_by_name(modulename: str) -> ModuleType:
    """
        Imports a module by name.
    """

    mod = None
    if modulename in sys.modules:
        mod = sys.modules[modulename]
    else:
        mod = importlib.import_module(modulename)

    return mod


def is_subclass_of_extension_factory(cand_type):
    """
        Returns a boolean value indicating if the candidate type is a subclass
        of :class:`ExtFactory`.
    """
    is_scoep = False
    if inspect.isclass(cand_type):
        if cand_type != ExtFactory and issubclass(cand_type, ExtFactory):
            is_scoep = True
    return is_scoep


def load_and_set_extension_factory_type(module_name: str):
    """
        Scans the module provided for :class:`ExtFactory` derived classes and will
        take the first one and assign it as the current runtime landscape type.
    """
    factory_type = None

    extpt_module = import_by_name(module_name)
    class_items = inspect.getmembers(extpt_module, is_subclass_of_extension_factory)

    extension_classes = []
    for _, cls_type in class_items:
        type_module_name = cls_type.__module__
        if type_module_name == extpt_module.__name__:
            extension_classes.append(cls_type)

    if len(extension_classes) > 1:
        wmsg = f"Only one ExtensionPoints class is allowed per module in order to perserve ordering. module={extpt_module}"
        logger.warning(wmsg)

    if len(extension_classes) > 0:
        factory_type = extension_classes[0]
    else:
        wmsg = f"Found extension module={extpt_module} without an `ExtensionPoints` derived class."
        logger.warning(wmsg)

    return factory_type