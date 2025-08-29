import pytest

from services.petstore.petstore_api import PetstoreApi

@pytest.mark.smoke
def test_get_pet():
    """Test getting pet details"""

    response = PetstoreApi.get_pet_by_id(pet_id=424242)
    assert response[0] == 200
    assert response[1].id == 1
