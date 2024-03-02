from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure

from tests.conftest import android_app_manage


def test_open_article_with_android(android_app_manage):
    with allure.step("Пропускаем ознакомительную страницу"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
    with allure.step("Кликаем по поиску"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Вставляем текст"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    with allure.step("Кликаем по первой статье"):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).first.click()
    with allure.step("В статье есть текст History"):
        browser.element((AppiumBy.XPATH,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.widget.TextView")).should(
            have.text("History"))
