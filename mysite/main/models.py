from django.db import models
from django.urls import reverse

class Parts(models.Model):
    title = models.CharField(max_length=255)
    alias = models.SlugField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="main/img/parts")
    price = models.CharField(max_length=20, default="Ціну уточнюйте")
    active = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_id': self.pk})

class Category(models.Model):
    name_cat = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name_cat

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
