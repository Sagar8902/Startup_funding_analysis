from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

@dataclass
class Business:
    name: str = None
    address: str = None
    phone_number: str = None

@dataclass
class BusinessList:
    business_list: list[Business] = field(default_factory=list)

    def dataframe(self):
        return pd.json_normalize((asdict(business) for business in self.business_list), sep='')

    def save_to_excel(self, filename):
        self.dataframe().to_excel(f'{filename}.xlsx', index=False)

    def save_to_csv(self, filename):
        self.dataframe().to_csv(f'{filename}.csv', index=False)

def scroll_page(page):
    page.evaluate("""() => {
        window.scrollBy(0, window.innerHeight);
    }""")

def main(search_for):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com/maps", timeout=600000)
        page.wait_for_timeout(1000)

        page.locator('//*[@id="searchboxinput"]').fill(search_for)
        page.wait_for_timeout(1000)

        page.keyboard.press("Enter")
        page.wait_for_timeout(1000)

        while True:
            scroll_height_before = page.evaluate("() => document.documentElement.scrollHeight")
            scroll_page(page)
            scroll_height_after = page.evaluate("() => document.documentElement.scrollHeight")
            if scroll_height_before == scroll_height_after:
                break

        page.wait_for_timeout(3000)

        listings = page.locator('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a')
        business_list = BusinessList()

        for listing in listings.element_handles():
            listing.click()
            page.wait_for_timeout(1000)

            name_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1'
            address_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div/div[2]/div[1]'
            phone_number_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/button/div/div[2]/div[1]'

            business = Business()
            business.name = page.locator(name_xpath).inner_text()
            business.address = page.locator(address_xpath).inner_text()
            business.phone_number = page.locator(phone_number_xpath).inner_text()

            business_list.business_list.append(business)

        save_filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
        if save_filename.endswith('.xlsx'):
            business_list.save_to_excel(save_filename)
        elif save_filename.endswith('.csv'):
            business_list.save_to_csv(save_filename)
        else:
            messagebox.showerror("Error", "Unsupported file format. Please save as .xlsx or .csv.")

        browser.close()

def start_scraper():
    search = search_entry.get()
    location = location_entry.get()
    search_for = f'{search} {location}' if location else search
    if search_for:
        main(search_for)
    else:
        messagebox.showerror("Error", "Please enter a search term.")

# GUI setup
root = tk.Tk()
root.title("Google Maps Data Scraper")

tk.Label(root, text="Search Term:").grid(row=0, column=0, padx=10, pady=10)
search_entry = tk.Entry(root)
search_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Location:").grid(row=1, column=0, padx=10, pady=10)
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Start Scraping", command=start_scraper).grid(row=2, columnspan=2, pady=10)

root.mainloop()


## check the xpath