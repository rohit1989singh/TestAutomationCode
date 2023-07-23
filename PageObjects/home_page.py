from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.XPATH, "//input[@title='Search for Products, Brands and More']")

    def navigate_to_homepage(self, url):
        self.driver.get(url)

    def enter_search_query(self, query):
        search_input = self.driver.find_element(*self.search_bar)
        search_input.clear()
        search_input.send_keys(query)

    def select_suggestion_by_mouse_action(self, suggestion_text):
        suggestion_locator = (By.XPATH, f"//a[contains(@href,'{suggestion_text}')]")

        suggestion_element = self.driver.find_element(*suggestion_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(suggestion_element).click().perform()
