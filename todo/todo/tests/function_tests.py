from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from todo.views import home


class HomeTestCase(TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

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

    def test_check_my_table(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: 공작깃털 사기', [row.text for row in rows])

        self.fail('finish the test!')
