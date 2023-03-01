from app.settings import Settings, init_settings
from app.api import create_app

settings = Settings()
init_settings(settings)  # initialize singleton (necessary?)
app = create_app(settings)
