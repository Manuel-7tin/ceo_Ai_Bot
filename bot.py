# Import all required libraries and packages
import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException, ElementClickInterceptedException,\
    StaleElementReferenceException

# Chabges to test streamlit: VChange 1

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
#

class ReviewBot:
    def __init__(self):
        self.id = 0
        self.driver = None
        self.business_reviews = {}
        self.reload_attempts = 0

    @st.cache_resource
    def get_driver(self, options):
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    def __initiate_bot(self):
        """Loads up bot web driver"""
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.reload_attempts = 0
        # VChange 2

        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        self.driver = self.get_driver(options)

    def get_reviews(self, index, link, num_of_links):
        """Retrieves reviews from Google"""
        if not self.id:
            self.__initiate_bot()
        names = []

        while True:
            print(f"Processing link {index+1} of {num_of_links}")
            if self.reload_attempts > (num_of_links * 1.5):
                print("Bot ran into a persistent error, Shutting Down")
                break
            try:
                # Open link in browser
                self.driver.get(link)
            except WebDriverException as e:
                print(f"Web driver error here: {e}")
                print("Reloading in 5 seconds....")
                self.reload_attempts += 1
                time.sleep(5)
            else:
                # Open review section
                try:
                    review_section = self.driver.find_element(By.ID, "reviews")
                    review_section.click()
                except NoSuchElementException:
                    print('review section unavailable')
                    break

                for k in range(2):
                    # Select available reviews
                    reviews = self.driver.find_elements(By.CLASS_NAME, "bwb7ce")
                    # print(f"total number of reviews caught is {len(reviews)}")
                    if not reviews:
                        print("No reviews caught, reloading in 5 seconds...")
                        self.reload_attempts += 1
                        time.sleep(5)
                        continue

                    # Expand a review to show more text
                    more_links = reviews[0].find_elements(By.TAG_NAME, "a")
                    for links in more_links:
                        if links.text == "More":
                            try:
                                links.click()
                            except ElementClickInterceptedException:
                                print("Unclickable element found")
                                continue
                            except StaleElementReferenceException:
                                print("Stale element error detected")
                                continue
                    gba = self.driver.find_elements(By.CLASS_NAME, "bwb7ce")
                    time.sleep(3)

                    for review in gba:
                        try:
                            text_div = review.find_element(By.CLASS_NAME, "OA1nbd")
                        except NoSuchElementException:
                            print(f"Element not found err")
                            continue
                        else:
                            names.append(text_div.text)

                    # Load more reviews
                    # scroll_bar = self.driver.find_element(
                    #     By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div'
                    # )
                    try:
                        scroll_bar = self.driver.find_element(By.CLASS_NAME, 'kKWzSd')
                    except NoSuchElementException:
                        continue

                    for j in (3, 1):
                        for i in range(j):
                            self.driver.execute_script(
                                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                scroll_bar)
                        time.sleep(4)
                if len(names) > 4 and names[0] == names[3]:
                    names = names[3:]
                self.business_reviews[index] = names
                self.id += 1
                break

    def destroy(self):
        """Terminates browser instance"""
        self.driver.quit()
