from pathlib import Path
import requests
import allure


def path():
    return str(Path(__file__).parent.parent.joinpath("source/app-alpha-universal-release.apk"))


@allure.step("Загружаем приложение и получаем ссылку")
def get_url_app(user_name, access_key, cloud_url):
    test_file = open(path(), "rb")
    response = requests.post(cloud_url, auth=(user_name, access_key),
                             files={"file": test_file})
    return response.json()["app_url"]
