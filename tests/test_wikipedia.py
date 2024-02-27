from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_wiki_article(mobile_manage):

    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).first.click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, "History")).should(have.text("History"))




