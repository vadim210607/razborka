# Generated by Django 4.1.7 on 2023-02-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='price',
            field=models.CharField(default='Ціну уточнюйте', max_length=20),
        ),
    ]
