from config.settings import PETSTORE_APP_SETTINGS
from models.petstore import PetstoreRequestModelPet, PetstoreResponseErrorModel
from services.api_client import ApiClient


class PetstoreApi:
    def __init__(self):
        self.base_url = PETSTORE_APP_SETTINGS["BASE_URL"]
        self.api_client = ApiClient(
            base_url=self.base_url,
            api_key=PETSTORE_APP_SETTINGS["API_KEY"]
        )
        self.add_new_pet_path = "/v2/pet"
        self.get_pet_by_id_path = "/v2/pet"

    def post_create_new_pet(self, request_data: PetstoreRequestModelPet):
        response = self.api_client.post(
            endpoint=self.add_new_pet_path,
            request_data=request_data,
            response_model=PetstoreRequestModelPet,
            response_error_model=PetstoreResponseErrorModel)
        return response

    def get_pet_by_id(self, pet_id):
        response = self.api_client.get(
            endpoint=f"{self.add_new_pet_path}/{pet_id}",
            response_model=PetstoreRequestModelPet,
            response_error_model=PetstoreResponseErrorModel)
        return response

    def put_update_existing_pet(self, request_data: PetstoreRequestModelPet):
        response = self.api_client.put(
            endpoint=self.add_new_pet_path,
            request_data=request_data,
            response_model=PetstoreRequestModelPet,
            response_error_model=PetstoreResponseErrorModel)
        return response


PetstoreApi: PetstoreApi = PetstoreApi()
