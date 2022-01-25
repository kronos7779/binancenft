from selenium.webdriver.common.by import By

from Config.config import TestData
from Config.config_cookies import cookies
from Pages import NftCollectionPage
from Pages.BasePage import BasePage


# from experiment.cookies import load_cookies


class SingleNftBuy(BasePage):

    single_nft_page = "https://www.binance.com/en/nft/goods/detail?productId=23400545&isProduct=1"
    buy_now_button = (By.XPATH, "//button[normalize-space()='Buy Now']")
    allow_button = (By.XPATH, "//button[contains(text(),'Accept')]")
    confirm = (By.XPATH, "//button[@class=' css-rtsl4l']")
    collections = (By.XPATH, "//button[normalize - space() = 'Collections']")
    failed_text = (By.XPATH, "//h6[contains(text(), 'Payment failed')]")
    return_button = (By.XPATH, "//button[normalize-space()='Return']")
    success_paid = (By.XPATH, "// h6[normalize - space() = 'Success paid']")

    def __init__(self, driver):
        super().__init__(driver)
        # cookies.load_cookies(self.driver, TestData.Cookie_location)
        # self.driver.get(self.single_nft_page)

    def is_visible_allow_button(self):
        return self.is_visible(self.allow_button)

    def click_allow_button(self):
        self.do_click(self.allow_button)

    def click_buy_now_button(self):
        self.do_click(self.buy_now_button)

    def is_visible_confirm_button(self):
        return self.is_visible(self.confirm)

    def click_confirm_button(self):
        self.do_click(self.confirm)

    def is_visible_collection_button(self):
        return self.is_visible(self.collections)

    def is_visible_payment_failed(self):
        return self.is_visible(self.failed_text)

    def click_return_button(self):
        self.do_click(self.return_button)


