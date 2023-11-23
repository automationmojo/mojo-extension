
import os

from mojo.startup.wellknown import StartupConfigSingleton

my_config = {}

startup_config = StartupConfigSingleton()
if "MOJO-EXTENSION" in startup_config:
    my_config = startup_config["MOJO-EXTENSION"]

class ExtensionConfiguration:

    MJR_CONFIGURED_FACTORY_MODULES = None
    if "MJR_CONFIGURED_FACTORY_MODULES" in os.environ:
        modules_as_path = os.environ["MJR_CONFIGURED_FACTORY_MODULES"]
        MJR_CONFIGURED_FACTORY_MODULES = set([m.strip() for m in modules_as_path.split(",")])
    elif "MJR_CONFIGURED_FACTORY_MODULES" in my_config:
        modules_as_path = my_config["MJR_CONFIGURED_FACTORY_MODULES"]
        MJR_CONFIGURED_FACTORY_MODULES = set([m.strip() for m in modules_as_path.split(",")])

    
