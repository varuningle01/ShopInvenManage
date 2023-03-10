# Generated by Django 3.2.7 on 2021-10-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_catsales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='cat_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='catsales',
            name='month',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(max_length=100),
        ),
    ]
