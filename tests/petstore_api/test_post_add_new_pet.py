import pytest

from models.petstore import PetstoreRequestModelPet, PetstoreRequestModelCategory, PetstoreRequestModelTag, \
    PetstoreRequestEnumStatus
from services.petstore.petstore_api import PetstoreApi

TEST_ID = 1
TEST_CAT_ID = 1
TEST_CAT_NAME = "Cat 1"
TEST_NAME = "Rex 1"
TEST_TAG_ID = 22
TEST_TAG_ID_2 = 23
TEST_TAG_NAME = "Tag 1"
TEST_TAG_NAME_2 = "Tag 2"
INVALID_INPUT = "Invalid input"
CLIENT_ERROR = "CLIENT_ERROR"


@pytest.mark.smoke
def test_post_add_new_pet_200_valid_data():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=TEST_CAT_NAME),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))
    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == TEST_CAT_ID
    assert response.body.category.name == TEST_CAT_NAME
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_405_id_string():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id="abc",
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=TEST_CAT_NAME),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))
    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT


def test_post_add_new_pet_200_id_null():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=None,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=TEST_CAT_NAME),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))
    assert response.code == 200
    assert response.body.id > 0
    assert response.body.category.id == TEST_CAT_ID
    assert response.body.category.name == TEST_CAT_NAME
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_200_category_null():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID, category=None,
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))
    assert response.code == 200
    assert response.body.id > 0
    assert response.body.category is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_405_category_string():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID, category=TEST_NAME,
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))
    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT


def test_post_add_new_pet_405_category_int():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID, category=TEST_CAT_ID,
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))
    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT


def test_post_add_new_pet_200_category_id_null():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=None, name=TEST_CAT_NAME),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 0
    assert response.body.category.name == TEST_CAT_NAME
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_405_category_id_string():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id="blabla", name=TEST_CAT_NAME),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT


def test_post_add_new_pet_200_category_name_null():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 1
    assert response.body.category.name is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_405_name_null():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=TEST_CAT_NAME),
                                             name=None, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT


def test_post_add_new_pet_405_photourls_null():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=TEST_CAT_NAME),
                                             name=TEST_NAME, photoUrls=None,
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT


def test_post_add_new_pet_200_photourls_single():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=["https://aa.a.com"],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 1
    assert response.body.category.name is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == ["https://aa.a.com"]
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_200_photourls_double():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=["https://aa.a.com", "https://bb.b.com"],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 1
    assert response.body.category.name is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == ["https://aa.a.com", "https://bb.b.com"]
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_200_tags_null():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=None,
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 1
    assert response.body.category.name is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert response.body.tags is None
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_200_tags_single_double():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME),
                                                   PetstoreRequestModelTag(id=TEST_TAG_ID_2, name=TEST_TAG_NAME_2)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 1
    assert response.body.category.name is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 2
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.tags[1].id == TEST_TAG_ID_2
    assert response.body.tags[1].name == TEST_TAG_NAME_2
    assert response.body.status == PetstoreRequestEnumStatus.PENDING.value


def test_post_add_new_pet_405_tags_invalid_data():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id="abc", name=TEST_TAG_NAME),
                                                   PetstoreRequestModelTag(id=TEST_TAG_ID_2, name=None)],
                                             status=PetstoreRequestEnumStatus.PENDING.value))

    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT


def test_post_add_new_pet_200_tags_status_available():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.AVAILABLE.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 1
    assert response.body.category.name is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.AVAILABLE.value


def test_post_add_new_pet_200_tags_status_sold():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.SOLD.value))

    assert response.code == 200
    assert response.body.id == TEST_ID
    assert response.body.category.id == 1
    assert response.body.category.name is None
    assert response.body.name == TEST_NAME
    assert response.body.photoUrls == []
    assert len(response.body.tags) == 1
    assert response.body.tags[0].id == TEST_TAG_ID
    assert response.body.tags[0].name == TEST_TAG_NAME
    assert response.body.status == PetstoreRequestEnumStatus.SOLD.value


def test_post_add_new_pet_405_tags_status_unknown():
    response = PetstoreApi.post_create_new_pet(
        request_data=PetstoreRequestModelPet(id=TEST_ID,
                                             category=PetstoreRequestModelCategory(id=TEST_CAT_ID, name=None),
                                             name=TEST_NAME, photoUrls=[],
                                             tags=[PetstoreRequestModelTag(id=TEST_TAG_ID, name=TEST_TAG_NAME)],
                                             status=PetstoreRequestEnumStatus.UNKNOWN_STRING.value))

    assert response.code == 405
    assert response.body.code == 405
    assert response.body.type == CLIENT_ERROR
    assert response.body.message == INVALID_INPUT
