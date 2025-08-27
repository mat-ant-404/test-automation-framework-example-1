import pytest

ADD_NEW_PET_PATH = "/v2/pet"


def test_create_new_pet(api_client):
    """Test creating a new pet"""


    response = api_client.post(ADD_NEW_PET_PATH, {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
    assert response["title"] == "Test Post"