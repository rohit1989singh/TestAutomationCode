import logging
from selenium import webdriver
from PageObjects.home_page import HomePage
from PageObjects.search_page import SearchPage


class ScriptExecution:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.setup_logging()
        logging.info("WebDriver initialized.")

    def setup_logging(self):
        logging.basicConfig(filename='script_log.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def navigate_to_homepage(self, url):
        self.home_page = HomePage(self.driver)
        self.home_page.navigate_to_homepage(url)
        logging.info(f"Navigated to the homepage: {url}")

    def enter_search_query(self, search_query):
        self.home_page.enter_search_query(search_query)
        self.driver.implicitly_wait(5)
        logging.info(f"Entered search query: {search_query}")

    def select_suggestion_by_mouse_action(self, suggestion_text):
        self.home_page.select_suggestion_by_mouse_action(suggestion_text)
        self.driver.implicitly_wait(5)
        logging.info(f"Selected suggestion: {suggestion_text}")

    def get_search_results(self):
        self.search_page = SearchPage(self.driver)
        logging.info("Fetching search results.")
        return self.search_page.get_search_results()

    def filter_best_sellers_and_trending(self, search_results):
        bestsellers = []
        trending = []

        for result in search_results:
            model_result = {"title": result["title"], "actual_price": result["actual_price"],
                            "discount": result["discount"], "selling_price": result["selling_price"]}
            if "Bestseller" in result["sales"]:
                bestsellers.append(model_result)
            elif "Trending" in result["sales"]:
                trending.append(model_result)
            else:
                continue

        return bestsellers, trending

    def print_details(self, bestsellers, trending):
        logging.info("Printing Bestseller Earphones Information:")
        bestsellers_data = []
        for id1, item in enumerate(bestsellers, 1):
            bestsellers_data.append(f"Model{id1}:{item}")
        logging.info(bestsellers_data)

        logging.info("\nPrinting Trending Earphones Information:")
        trending_data = []
        for id2, item in enumerate(trending, 1):
            trending_data.append(f"Model{id2}:{item}")
        logging.info(trending_data)

    def close_browser(self):
        self.driver.quit()
        logging.info("WebDriver closed.")

if __name__ == "__main__":
    script_execution = ScriptExecution()

    url = "https://www.flipkart.com/"
    search_query = "boat bluet"
    suggestion_text = "boat+bluetooth+earphone"

    script_execution.navigate_to_homepage(url)
    script_execution.enter_search_query(search_query)
    script_execution.select_suggestion_by_mouse_action(suggestion_text)

    search_results = script_execution.get_search_results()
    bestsellers, trending = script_execution.filter_best_sellers_and_trending(search_results)

    script_execution.print_details(bestsellers, trending)

    script_execution.close_browser()
