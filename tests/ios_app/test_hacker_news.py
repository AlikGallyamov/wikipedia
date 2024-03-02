from appium.webdriver.common.appiumby import AppiumBy
import allure
from selene import browser, have


def test_open_page(ios_app_manage):
    with allure.step("Кликаем по кнопке"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
    with allure.step("Вставляем текст"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("hello@browserstack.com" + "\n")
    with allure.step("В поле отображается текст hello@browserstack.com"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("hello@browserstack.com"))
