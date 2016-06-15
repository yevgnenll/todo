from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from todo.views import home


class HomeTestCase(TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')

    def tearDown(self):

        self.browser.quit()

    def test_home_page_can_save_a_POST_request(self):

        # setting
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        # exercise
        response = home(request)

        # assert
        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'},
            request=request,
        )
        self.assertEqual(response.content.decode(), expected_html)

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

        self.fail('finish the test!')
