from django.test import LiveServerTestCase

from lists.models import Item


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
