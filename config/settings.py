import os

PETSTORE_APP_SETTINGS = {
    "BASE_URL": "https://petstore.swagger.io",
    "API_KEY": os.environ.get("TAF_PETSTORE_API_KEY")
}

TEST_METADATA = {
    "TESTER_FULLNAME": os.environ.get("TAF_TESTER_FULLNAME"),
    "TEST_ENV": os.environ.get("TAF_TEST_ENVIRONMENT")
}