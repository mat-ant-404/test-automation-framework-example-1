import os

PETSTORE_APP_SETTINGS = {
    "BASE_URL": "https://petstore.swagger.io",
    "API_KEY": os.environ.get("PETSTORE_API_KEY")
}
