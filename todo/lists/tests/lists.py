from django.test import LiveServerTestCase
from django.http import HttpRequest

from lists.models import Item
from todo.views import home


class ItemModelTest(LiveServerTestCase):

    def test_saving_and_retrieving_items(self):

        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]

        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_item.text, '두 번째 아이템')

    def test_home_page_can_save_a_POST_request(self):

        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.last()
        self.assertEqual(new_item.text, '신규 작업 아이템')


class ListViewTest(LiveServerTestCase):

    def test_uses_list_template(self):

        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_display_all_list_items(self):

        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        request = HttpRequest()
        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
