from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_open_article_with_android(android_app_manage):
    with allure.step("Отображается The Free Encyclopedia …in over 300 languages"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/secondaryTextView")).should(
            have.text("We’ve found the following on your device:"))
    with allure.step("Кликаем Continue"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
    with allure.step("Отображается New ways to explore"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("New ways to explore"))
    with allure.step("Кликаем Continue"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
    with allure.step("Отображается Reading lists with sync"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("Reading lists with sync"))
    with allure.step("Кликаем Continue"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
    with allure.step("Отображается Data & Privacy"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Data & Privacy"))



