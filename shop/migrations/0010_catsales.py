# Generated by Django 3.2.7 on 2021-10-04 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_item_cat_gar'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('sales', models.IntegerField()),
                ('profit', models.IntegerField()),
                ('cat_sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categories')),
            ],
            options={
                'db_table': 'profit_sales',
            },
        ),
    ]