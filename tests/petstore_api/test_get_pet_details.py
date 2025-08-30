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

    assert response.code == 200
    assert response.body.id == 23
    assert response.body.category.id == 0
    assert response.body.category.name == "dog"
    assert response.body.name == "Max Whiskers"
    assert response.body.photoUrls == ["string"]
    assert response.body.tags[0].id == 0
    assert response.body.tags[0].name == "puppy"
    assert response.body.status in [PetstoreRequestEnumStatus.PENDING.value, PetstoreRequestEnumStatus.AVAILABLE.value,
                                  PetstoreRequestEnumStatus.SOLD.value]


def test_get_pet_details_404_non_existing_pet():
    response = PetstoreApi.get_pet_by_id(pet_id=0)

    assert response.code == 404
    assert response.body.code == 1
    assert response.body.type == TYPE_ERROR
    assert response.body.message == NOT_FOUND_MESSAGE
