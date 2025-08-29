# test-automation-framework-example-1
API test automation framework

## Framework prerequisites and installation -> using Pycharm
- Python 3.13 installed -> https://www.python.org/downloads/release/python-3120/
- Python added to PATH
- from projectroot execute -> "python -m venv taf" (creating virtualenv named taf1)
- from projectroot execute -> ".\taf1\Scripts\activate" (activate virtualenv named taf1)
- from projectroot execute -> ".\taf1\Scripts\activate" (activate virtualenv named taf1)
- in Pycharm - File - Settings - Python - Interpreter -> add existing interpreter (python executable from virtualenv taf1)

## Using tests -> How to (run)
- PETSTORE_API_KEY needs to be added to environment variables
- tests can be run by using run/debug option in Pycharm
- tests can be run by executing command "pytest" from project root
- only smoke tests can be executed with "pytest -m smoke" from project root
- html report and log file will be created when tests are executed, they get save din output folder