from django.db import models
from django.urls import reverse


#                  ________PARTS_________

class Parts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo", default="no_image.png", verbose_name="Фото")
    price = models.CharField(max_length=20, default="Ціну уточнюйте", verbose_name="Ціна")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name="Активне")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    auto = models.ManyToManyField('Auto')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

    def parts_first_image(self):
        return self.parts_images.first()

    class Meta:
        verbose_name = 'Автозапчастину'
        verbose_name_plural = 'Автозапчастини'
        ordering = ['time_create', 'title']

def part_image_path(instance, filename):
    return 'photo/{0}/{1}'.format(instance.parts.slug, filename)


class Partsimage(models.Model):
    # image = models.ImageField(upload_to="photo/galery")
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

#                    _________AUTO___________


class Auto(models.Model):
    auto = models.CharField(max_length=50, db_index=True, verbose_name="Модель")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.auto

    def get_absolute_url(self):
        return reverse('auto', kwargs={'auto_id': self.pk})

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'


