
import os

class ExtensionConfiguration:

    CONFIGURED_FACTORY_MODULES = None
    if "CONFIGURED_FACTORY_MODULES" in os.environ:
        modules_as_path = os.environ["CONFIGURED_FACTORY_MODULES"]
        CONFIGURED_FACTORY_MODULES = set(modules_as_path.split(","))
