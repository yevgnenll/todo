from django.test import LiveServerTestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from todo.views import home
from lists.models import Item


class HomeTestCase(LiveServerTestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):

        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        # find to_do list in table

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_check_my_table(self):

        self.assertIn('To-Do', self.browser.title)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')
