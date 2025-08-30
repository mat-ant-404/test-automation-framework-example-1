# test-automation-framework-example-1

API test automation framework

## Framework prerequisites and installation -> using Pycharm

- Python 3.13 installed -> https://www.python.org/downloads/release/python-3120/
- Python added to PATH
- from project root execute -> "python -m venv taf" (creating virtualenv named taf1)
- from project root execute -> ".\taf1\Scripts\activate" (activate virtualenv named taf1)
- in Pycharm - File - Settings - Python - Interpreter -> add existing interpreter (python executable from virtualenv
  taf1)
- from project root execute -> "pip install -r requirements.txt"

## Executing tests and checking results

- TAF_PETSTORE_API_KEY must be added to environment variables, otherwise api_key won't be sent in request headers
- TAF_TESTER_FULLNAME must be added to environment variables, otherwise "Tester" will be "Not provided" in html report
- TAF_TEST_ENVIRONMENT must be added to environment variables, otherwise "Environment name" will be "Not provided" in html report
- tests can be run by using run/debug option in Pycharm in debug purposes
- tests are correctly run by executing command "pytest" from project root
- only smoke tests can be executed with "pytest -m smoke" from project root
- html report and log file will be created as a pair with same name (except extension) when tests are executed, they get
  saved in output folder