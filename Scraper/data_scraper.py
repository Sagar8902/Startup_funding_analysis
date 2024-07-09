from playwright.sync_api import sync_playwright
from dataclasses import dataclass,asdict,field
import pandas as pd
import argparse

@dataclass
class Business:
    name:str = None
    address:str = None
    phone_number:str = None

@dataclass
class BusinessList:
    business_List : list[Business] = field(default_factory=list)

    def dataframe(self):
        return pd.json_normalize((asdict(business) for business in self.business_List),sep='')

    def save_to_excel(self,filename):
        self.dataframe().to_excel(f'{filename}.xlsx',index=False)

    def save_to_csv(self,filename):
        self.dataframe().to_csv(f'{filename}.csv',index=False)

def main():

    def scroll_page(page):
        page.evaluate("""() => {
            window.scrollBy(0, window.innerHeight);
        }""")

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False) # < default True
        page = browser.new_page()

        page.goto("https://www.google.com/maps",timeout=60000) # 60 sec timeoutlimit
        page.wait_for_timeout(5000) # we can remove this

        page.locator('//*[@id="searchboxinput"]').fill(search_for)
        page.wait_for_timeout(5000) # we can write upto 1 sec or remove it

        page.keyboard.press("Enter")
        page.wait_for_timeout(2000)

        while True:
            scroll_height_before = page.evaluate("() => document.documentElement.scrollHeight")
            scroll_page(page)
            scroll_height_after = page.evaluate("() => document.documentElement.scrollHeight")
            if scroll_height_before == scroll_height_after:
                break  # Stop scrolling if we reach the bottom of the page

        page.wait_for_timeout(3000)

        listings = page.locator('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a')
        # print(len(listings))

        business_list = BusinessList()

        for listing in listings:

            listing.click()
            page.wait_for_timeout(2000)

            name_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1'
            address_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div/div[2]/div[1]'
            phone_number_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/button/div/div[2]/div[1]'

            business = Business()
            business.name = page.locator(name_xpath).inner_text()
            business.address = page.locator(address_xpath).inner_text()
            business.phone_number = page.locator(phone_number_xpath).inner_text()

            business_list.business_List.append(business)

        business_list.save_to_excel("google_data_scrape.xlsx")
        business_list.save_to_csv("google_data_scrape.csv")

        browser.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--search",type=str)
    parser.add_argument("-l","--location",type=str)
    args = parser.parse_args()

    if args.location and args.search:
        search_for = (f'{args.search} {args.location}')
    else:
        search_for = "plant nursery india"

    main()


