# Generated by Django 4.1.7 on 2023-04-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_parts_title_ru_parts_title_uk_alter_partsimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='auto_ru',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='auto',
            name='auto_uk',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_ru',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_uk',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Категорія'),
        ),
    ]