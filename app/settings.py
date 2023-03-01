import logging
from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    http_host: str = Field("0.0.0.0")
    http_port: int = Field(8080)
    log_level: str = Field("INFO")

    # pylint: disable=no-self-argument,no-self-use,protected-access
    @validator("log_level")
    def _validate_log_level(cls, v):
        v_upper = v.upper()
        if v_upper not in logging._nameToLevel:
            raise ValueError(f'invalid value "{v}"')
        return v_upper


# will be initialized on startup
_settings = None


# pylint: disable=global-statement
def init_settings(settings: Settings):
    global _settings
    if _settings is not None:
        raise RuntimeError("settings already initialized")
    # kwargs override environment variables
    _settings = settings


def get_settings():
    if _settings is None:
        raise RuntimeError("settings not initialized")
    return _settings
