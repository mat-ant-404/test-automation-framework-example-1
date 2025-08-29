import pytest

from models.petstore import PetstoreRequestEnumStatus
from services.petstore.petstore_api import PetstoreApi

TEST_ID = 1
TEST_CAT_ID = 1
TEST_CAT_NAME = "Cat 1"
TEST_NAME = "Rex 1"
TEST_TAG_ID = 22
TEST_TAG_ID_2 = 23
TEST_TAG_NAME = "Tag 1"
TEST_TAG_NAME_2 = "Tag 2"
NOT_FOUND_MESSAGE = "Pet not found"
TYPE_ERROR = "error"


@pytest.mark.smoke
def test_get_pet_details_200_valid():
    response = PetstoreApi.get_pet_by_id(pet_id=23)

    assert response[0] == 200
    assert response[1].id == 23
    assert response[1].category.id == 0
    assert response[1].category.name == "dog"
    assert response[1].name == "Max Whiskers"
    assert response[1].photoUrls == ["string"]
    assert response[1].tags[0].id == 0
    assert response[1].tags[0].name == "puppy"
    assert response[1].status in [PetstoreRequestEnumStatus.PENDING.value, PetstoreRequestEnumStatus.AVAILABLE.value,
                                  PetstoreRequestEnumStatus.SOLD.value]


def test_get_pet_details_404_non_existing_pet():
    response = PetstoreApi.get_pet_by_id(pet_id=0)

    assert response[0] == 404
    assert response[1].code == 1
    assert response[1].type == TYPE_ERROR
    assert response[1].message == NOT_FOUND_MESSAGE
