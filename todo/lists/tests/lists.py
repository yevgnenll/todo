from django.test import LiveServerTestCase
from django.http import HttpRequest

from lists.models import Item, Inventory
from todo.views import home


class ItemModelTest(LiveServerTestCase):

    def test_saving_and_retrieving_items(self):

        inven = Inventory.objects.create()

        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.inven = inven
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.inven = inven
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]

        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_item.text, '두 번째 아이템')


class ListViewTest(LiveServerTestCase):

    def test_uses_list_template(self):

        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_display_all_list_items(self):

        inven = Inventory.objects.create()

        Item.objects.create(text='itemey 1', inven=inven)
        Item.objects.create(text='itemey 2', inven=inven)

        request = HttpRequest()
        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
