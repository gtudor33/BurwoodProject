import os
from dynaconf import Dynaconf

# TODO: in case we want to expand we should use configs for deploying the app.
settings_file = os.getenv("CONFIG_FILE")
settings = Dynaconf(envvar_prefix=False, settings_files=[settings_file])
settings.app_name = "app"
