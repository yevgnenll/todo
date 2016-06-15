from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomeTestCase(TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):

        self.browser.quit()

    def test_check_my_table(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
        )

        self.fail('finish the test!')
