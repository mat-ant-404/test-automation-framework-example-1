import pytest
from services.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    base_url = "https://petstore.swagger.io"


    return ApiClient(
        base_url=base_url
    )
