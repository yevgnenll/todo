from django.db import models


class Inventory(models.Model):
    pass


class Item(models.Model):

    text = models.TextField(default='')
    inven = models.ForeignKey(
        Inventory,
        default=None,
    )

    def __str__(self):

        return "{inven}-{id}: {text}".format(
            inven=self.inven,
            id=self.id,
            text=self.text,
        )
