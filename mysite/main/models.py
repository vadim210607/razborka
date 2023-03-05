from django.db import models
from django.urls import reverse

class Parts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва")
    alias = models.SlugField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo", default="no_image.png", verbose_name="Фото")
    price = models.CharField(max_length=20, default="Ціну уточнюйте", verbose_name="Ціна")
    # time_create = models.DateTimeField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name="Активне")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    auto = models.ForeignKey('Auto', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('parts', kwargs={'parts_id': self.pk})

    class Meta:
        verbose_name = 'Автозапчастину'
        verbose_name_plural = 'Автозапчастини'
        # ordering = ['time_create', 'title'] 5555555555555555 зробить поле тайм креате


class Category(models.Model):
    category = models.CharField(max_length=50, db_index=True, verbose_name="Категорія")

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'


class Auto(models.Model):
    auto = models.CharField(max_length=50, db_index=True, verbose_name="Модель")

    def __str__(self):
        return self.auto

    def get_absolute_url(self):
        return reverse('auto', kwargs={'auto_id': self.pk})

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'


