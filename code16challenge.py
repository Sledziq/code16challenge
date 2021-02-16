from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

DRIVER_PATH = r'./chromedriver.exe'
amount = 128
driver = webdriver.Chrome(DRIVER_PATH)
def button_from_list_click(button_list, button_name):
    for button in button_list:
        if button.text == button_name:
            button.click()
            break

driver.get('https://www.siepomaga.pl/code16challenge')
try:
    support_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'sp-button.big.red.with-white-heart.animated.full-width')))
finally:
    support_button.click()
try:
    amount_buttons = WebDriverWait(driver, 5). until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'amount-button')))
finally:
    button_from_list_click(amount_buttons, 'Inna kwota')
    amount_field = driver.find_element_by_id('other_amount')
    amount_field.clear()
    amount_field.send_keys(amount)
checkbox_list = driver.find_elements_by_class_name('checkbox')
button_from_list_click(checkbox_list, 'Wpłata anonimowa')
pay_button = driver.find_element_by_id('pay_now')
pay_button.click()
