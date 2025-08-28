import pytest

from models.petstore import PetstoreRequestModelPet
from services.petstore.petstore_api import PetstoreApi


@pytest.mark.smoke
def test_create_new_pet():
    """Test creating a new pet"""

    response = PetstoreApi.post_create_new_pet(request_data=PetstoreRequestModelPet(id=1))
    assert response[0] == 200
    assert response[1].id == 1

@pytest.mark.smoke
def test_get_pet():
    """Test creating a new pet"""

    response = PetstoreApi.get_pet_by_id(pet_id=424242)
    assert response[0] == 200
    assert response[1].id == 1

@pytest.mark.smoke
def test_update_pet():
    """Test creating a new pet"""

    response = PetstoreApi.put_update_existing_pet(request_data=PetstoreRequestModelPet(id=1))
    assert response[0] == 200
    assert response[1].id == 1