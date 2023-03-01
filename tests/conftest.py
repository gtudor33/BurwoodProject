# pylint: disable=redefined-outer-name
import pytest
from httpx import AsyncClient
import respx

from app import create_app, Settings
from app.settings import get_settings


@pytest.fixture(scope="session")
def settings():
    return Settings()


@pytest.fixture(scope="session")
def app(settings):
    app = create_app(settings)
    app.dependency_overrides[get_settings] = lambda: settings
    return app


@pytest.fixture
def client(app):
    respx.route(host="test").pass_through()
    aclient = AsyncClient(app=app, base_url="http://test")
    return aclient
