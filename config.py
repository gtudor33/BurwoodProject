import os
from dynaconf import Dynaconf

settings_file = os.getenv("CONFIG_FILE")
settings = Dynaconf(envvar_prefix=False, settings_files=[settings_file])
settings.app_name = "app"
