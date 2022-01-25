import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import TestData
from Config.config_cookies import cookies
from Pages.BasePage import BasePage


# from experiment.cookies import load_cookies


class NftCollectionPage(BasePage):
    # Real Collection
    collection_link = "https://www.binance.com/en/nft/shopWindow/NFT%E2%96%B5PRIDE?reSale=0&tradeType=0&orderBy=list_time&orderType=-1&isBack=1&uid=aa80c3015e02724438bd7cb9e662c5b8&order=list_time%40-1"
    # Low price NFT collection
    # collection_link = "https://www.binance.com/en/nft/shopWindow/Honyx?reSale=0&tradeType=0&currency=BUSD&orderBy=amount_sort&orderType=1&isBack=1&uid=e43e7da3bc0733ce6978dbe7db14bac1&order=amount_sort%401"



    allow_button = (By.XPATH, "//button[contains(text(),'Accept')]")
    search_box = (By.XPATH, "//input[@placeholder='Search items']")
    search_text = "ape"
    currency_input = (By.XPATH, "(//*[name()='svg'][@class='css-a4o4go'])[3]")
    min_value_box = (By.XPATH, "//div[@class='css-824fpy']//div[1]//input[1]")
    min_value = '55'
    nft_list = (By.XPATH, "//div[@class='css-8a1dsu']")
    ok_button = (By.XPATH, "//button[normalize-space()='OK']")
    confirm_pop_up = (By.XPATH,)

    def __init__(self, driver):
        super().__init__(driver)
        # cookies.load_cookies(self.driver, TestData.Cookie_location)
        # self.driver.get(self.collection_link)

    def get_search_page_title(self, title):
        return self.get_title(title)

    def is_visible_allow_button(self):
        return self.is_visible(self.allow_button)

    def click_allow_button(self):
        self.do_click(self.allow_button)

    def is_visible_search_box(self):
        return self.is_visible(self.search_box)

    def input_search(self):
        self.do_send_keys(self.search_box, self.search_text)

    def click_currency(self):
        self.do_click(self.currency_input)

    def input_min(self):
        self.do_send_keys(self.min_value_box, self.min_value)

    def find_nft(self):
        elements = WebDriverWait(self.driver, 1).until(EC.visibility_of_all_elements_located(self.nft_list))
        return elements

    def single_nft_tab(self):
        self.new_window(self.nft_list)

    def click_ok_button(self):
        self.do_click(self.ok_button)
