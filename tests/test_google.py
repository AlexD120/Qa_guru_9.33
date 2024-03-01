from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=2)

driver.get('https://google.com/ncr')


def find_element(driver):
    return driver.find_element(By.CSS_SELECTOR, '[name="q"]')


wait.until(find_element).send_keys('selene', Keys.ENTER)
