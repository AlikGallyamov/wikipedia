from pathlib import Path
import requests


def path():
    return str(Path(__file__).parent.parent.joinpath("source/app-alpha-universal-release.apk"))


def get_url_app():
    user_name = "azgallyamov_0wTr3j"
    access_key = "mckBkK9h5XxxhVcXBnpq"
    test_file = open(path(), "rb")
    response = requests.post("https://api-cloud.browserstack.com/app-automate/upload", auth=(user_name, access_key),
                             files={"file": test_file})
    return response.json()["app_url"]
