import pytest

from config.settings import PETSTORE_APP_SETTINGS
from services.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client_petstore():
    base_url = PETSTORE_APP_SETTINGS["BASE_URL"]
    return ApiClient(
        base_url=base_url,
    )
