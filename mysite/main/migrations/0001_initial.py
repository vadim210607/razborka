# Generated by Django 4.1.7 on 2023-03-02 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto', models.CharField(db_index=True, max_length=50, verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Моделі',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=50, verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Категорію',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('alias', models.SlugField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(default='no_image.png', upload_to='photo', verbose_name='Фото')),
                ('price', models.CharField(default='Ціну уточнюйте', max_length=20, verbose_name='Ціна')),
                ('active', models.BooleanField(default=True, verbose_name='Активне')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.auto')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
            options={
                'verbose_name': 'Автозапчастину',
                'verbose_name_plural': 'Автозапчастини',
            },
        ),
    ]
