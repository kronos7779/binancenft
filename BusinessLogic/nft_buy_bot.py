import time

from selenium.webdriver.common.by import By

from Bots.AllPageBot import AllPageBot
from Pages.NftCollectionPage import NftCollectionPage

# Time Counting
from Pages.SingleNftBuy import SingleNftBuy

StartTime = time.time()
print("This Script Start " + time.ctime())

all_page = AllPageBot()


# try:
#     login = all_page.login()
#     print(input("Press any Key: "))
# except:
#     print("You already lodged in")

# single nft page
all_page.driver.get("https://www.binance.com/en/nft/home")
print(input("Set Password : "))

# TODO: find nft
all_page.driver.get(NftCollectionPage.collection_link)
print(input("Filter done:"))


def after_payment(success, payment_failed):
    if len(success) == 1:
        # print(success[0].text)
        print("This function working")
    elif len(payment_failed) == 1:
        print(payment_failed[0].text)
        all_page.test_click_return_button()
        all_page.test_click_confirm_button()


def ok_button():
    for i in range(3):
        print(i)
        all_page.test_click_ok_button()
        time.sleep(2)


def switch_tab_to_single_nft(driver):
    start_tab_time = time.time()
    window_before = driver.window_handles[0]
    # TODO : Got Error
    """ here window_after = driver.window_handles[1] IndexError: list index out of range """
    window_after = driver.window_handles[1]

    if driver.window_handles[1] == window_after:
        driver.switch_to.window(window_after)

        # print(input("Change NFT for tasting :"))
        # all_page.driver.get("https://www.binance.com/en/nft/goods/detail?productId=23911067&isProduct=1")
        # print(input("Close Tab :"))

        sold_out_xpath = "//button[normalize-space()='Sold Out']"
        if all_page.driver.find_element_by_xpath(sold_out_xpath):
            print("NFT sold out go bach to search")
            # print(input("Find the Sold out button :"))
            driver.close()
            driver.switch_to.window(window_before)

        else:
            print(" I am buying")
            all_page.test_click_confirm_button()

            success_paid_xpath = "//div[@class='css-57wjep']"
            success = all_page.driver.find_elements(By.XPATH, success_paid_xpath)

            payment_failed_xpath = "//h6[contains(text(), 'Payment failed')]"
            payment_failed = all_page.driver.find_elements(By.XPATH, payment_failed_xpath)

            after_payment(success, payment_failed)

            driver.close()
            driver.switch_to.window(window_before)


        CurrentTime = time.time()
        totalRunningTime = CurrentTime - start_tab_time
        print("This Tab is running for " + str(float(totalRunningTime)))
    else:
        driver.switch_to.window(window_before)
        print(" Didn't find Second Tab")


# Repeat the process
buying_start_time = time.time()

for idx in range(6000):
    search_loop_start_time = time.time()
    try:
        nft_list = all_page.test_find_nft()
    except:
        nft_list = ''
    # print(nft_list)
    nft_numbers = len(nft_list)
    if nft_numbers >= 1:
        print(f"{idx + 1} no search working and {nft_numbers} nft found")
        for nft in range(0, len(nft_list)):
            loop_start_time = time.time()
            nft_list[nft].click()
            switch_tab_to_single_nft(all_page.driver)

            ok_button()

            # TODO: Base on nft no. we wll open tabs and buy all the nft together
            CurrentTime = time.time()
            totalRunningTime = CurrentTime - loop_start_time
            print("This Loop is running for " + str(float(totalRunningTime)))
            print("................")
    else:

        print(f"{idx + 1} no search working, No nft found ")
        all_page.test_click_ok_button()
        CurrentTime = time.time()
        totalRunningTime = CurrentTime - search_loop_start_time
        print("This Search is running for " + str(float(totalRunningTime)))

        totalBuyingTime = CurrentTime - buying_start_time
        print("This Total Process is running less than " + str(float(totalBuyingTime / 60)) + " Minutes.\n")

# TODO: go to collection

EndTime = time.time()
print("\nThis Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
