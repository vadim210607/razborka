from django.db import models
from django.urls import reverse


#                  ________PARTS_________

class Parts(models.Model):
    parts = models.CharField(max_length=255, verbose_name="Назва")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
#    photo = models.ImageField(upload_to="photo", default="no_image.png", verbose_name="Фото")
    price = models.CharField(max_length=20, default="Ціну уточнюйте", verbose_name="Ціна")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name="Активне")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    model = models.ManyToManyField('Model')

    def __str__(self):
        return self.parts

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

    def parts_first_image(self):
        return self.parts_images.first()

    class Meta:
        verbose_name = 'Автозапчастину'
        verbose_name_plural = 'Автозапчастини'
        ordering = ['time_create', 'parts']


def part_image_path(instance, filename):
    return 'photo/{0}-{1}/{2}'.format(instance.parts.id, instance.parts.slug, filename)


class PartsImage(models.Model):
#   image = models.ImageField(upload_to="photo/galery")
    image = models.ImageField(upload_to=part_image_path)
    parts = models.ForeignKey(Parts, on_delete=models.CASCADE, related_name='parts_images')

#                    _________CATEGORY___________


class Category(models.Model):
    category = models.CharField(max_length=50, db_index=True, verbose_name="Категорія")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

#                    _________ MODEL ___________


class Model(models.Model):
    model = models.CharField(max_length=50, db_index=True, verbose_name="Модель")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('model', kwargs={'model_id': self.pk})

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'


