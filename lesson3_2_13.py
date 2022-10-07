import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

link_one = "http://suninjuly.github.io/registration1.html"
link_two = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()


class TestAbs(unittest.TestCase):
    def find_el_by_css(self, selector):
        element_looking_for = browser.find_element(By.CSS_SELECTOR, selector)
        return element_looking_for

    def registration_test(self, link):
        browser.get(link)
        first_name = self.find_el_by_css(".first_block > .form-group.first_class > .form-control.first")
        first_name.send_keys("Imya")

        last_name = self.find_el_by_css(".first_block > .form-group.second_class > .form-control.second")
        last_name.send_keys("Familiya")

        email_field = self.find_el_by_css(".first_block > .form-group.third_class > .form-control.third")
        email_field.send_keys("email@email.com")

        submit_btn = self.find_el_by_css(".btn.btn-default")
        submit_btn.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_link_one(self):
        self.registration_test(link_one)

    def test_link_two(self):
        self.registration_test(link_two)