from selenium.webdriver.common.by import By
import time


def test_check_button_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	browser.get(link)
	time.sleep(30)
	find_button_basket = browser.find_element(By.XPATH, "//a[contains(@href, '/basket/')]")
	
	