from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def made_cart(self):
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#first-name")
        text_input.send_keys("Марина")

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#last-name")
        text_input.send_keys("Игамназарова")

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#postal-code")
        text_input.send_keys("352680")

        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

        total_cost = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        total_cost_value = float(total_cost.split("$")[1])

        assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, но получена {total_cost_value}"



