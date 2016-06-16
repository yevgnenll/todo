from django.test import LiveServerTestCase
from django.http import HttpRequest
from django.core.urlresolvers import reverse

from todo.views import home
from lists.models import Item, Inventory


class NewListTest(LiveServerTestCase):

    def test_saving_a_POST_request(self):

        # 직업 post를 보내는 방식
        self.client.post(
            reverse('new'),
            data={
                'item_text': '신규 작업 아이템',
            },
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

    def test_redirects_after_POST(self):

        response = self.client.post(
            reverse('new'),
            data={
                'item_text': '신규 작업 아이템',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('only'))
