import re
from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.cards = "div.col-2-12 ~ div div.col-12-12 div[data-id]"
        self.title_selector = "a.s1Q9rs"
        self.actual_price_selector = "div._3I9_wc"
        self.discount_selector = "div._3Ay6Sb"
        self.selling_price_selector = "div._30jeq3"

    def get_search_results(self):
        cards = self.driver.find_elements(By.CSS_SELECTOR, self.cards)
        results = []

        for card in cards:
            title = card.find_element(By.CSS_SELECTOR, self.title_selector).text
            actual_price = card.find_element(By.CSS_SELECTOR, self.actual_price_selector).text
            discount = card.find_element(By.CSS_SELECTOR, self.discount_selector).text
            selling_price = card.find_element(By.CSS_SELECTOR, self.selling_price_selector).text

            if len(re.findall("BestsellerId", card.get_attribute("innerHTML"))) >= 3:
                content = "Bestseller"
            elif len(re.findall("TrendingId", card.get_attribute("innerHTML"))) >= 3:
                content = "Trending"
            else:
                content = "ad"

            results.append({"sales":content, "title": title, "actual_price": actual_price, "discount": discount,
                            "selling_price": selling_price})
        return results
