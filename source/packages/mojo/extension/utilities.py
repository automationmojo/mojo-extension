"""
.. module:: utilities
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains utility functions used to scan for extension modules
               and factory types.

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

from typing import List

import importlib
import inspect
import logging
import os
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

def scan_mojo_factories_namespace() -> List[str]:

    search_paths = set([p for p in sys.path])

    rel_mojo_factories =  os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    search_paths.add(rel_mojo_factories)

    modules_found = []

    for dir_path in search_paths:
        check_dir = os.path.join(dir_path, "mojo", "factories")
        if os.path.exists(check_dir) and os.path.isdir(check_dir):
            check_dir_modules = scan_for_descendant_modules(check_dir)
            modules_found.extend(check_dir_modules)

    return modules_found

def scan_for_descendant_modules(scan_dir: str, module_prefix: str="mojo.factories") -> List[str]:

    modules_found = []

    for dirpath, dirnames, filenames in os.walk(scan_dir):
        leafpath = dirpath[len(scan_dir):].strip(os.sep)
        leafpath_parts = []
        if len(leafpath) > 0:
            leafpath_parts = dirpath.split(os.sep)

        for fname in filenames:
            if fname.endswith(".py"):
                fcomp = fname[:-3]
                mod_parts_comp = ""
                if len(leafpath_parts) > 0:
                    mod_parts_comp = "." + ".".join(leafpath_parts)

                mod_name = f"{module_prefix}{mod_parts_comp}.{fcomp}"
                modules_found.append(mod_name)

    return modules_found