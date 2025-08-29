import pytest

from models.petstore import PetstoreRequestModelPet
from services.petstore.petstore_api import PetstoreApi


@pytest.mark.smoke
def test_update_pet():
    """Test updating a pet"""
    response = PetstoreApi.put_update_existing_pet(request_data=PetstoreRequestModelPet(id=1))
    assert response[0] == 200
    assert response[1].id == 1