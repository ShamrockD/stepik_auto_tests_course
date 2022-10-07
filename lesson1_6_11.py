from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

link_one = "http://suninjuly.github.io/registration1.html"  # первая ссылка, которая проходит тест
link_two = "http://suninjuly.github.io/registration2.html"  # вторая ссылка, которая не проходит тест


def find_el_by_css(selector):
    element_looking_for = browser.find_element(By.CSS_SELECTOR, selector)
    return element_looking_for


try:
    browser.get(link_one)  # меняем link_one и link_two для разных результатов.

    first_name = find_el_by_css(".first_block > .form-group.first_class > .form-control.first")
    first_name.send_keys("Imya")

    last_name = find_el_by_css(".first_block > .form-group.second_class > .form-control.second")
    last_name.send_keys("Familiya")

    email_field = find_el_by_css(".first_block > .form-group.third_class > .form-control.third")
    email_field.send_keys("email@email.com")

    submit_btn = find_el_by_css(".btn.btn-default")
    submit_btn.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
