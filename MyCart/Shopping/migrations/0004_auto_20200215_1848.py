# Generated by Django 3.0.2 on 2020-02-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='Shopping/static/images'),
        ),
    ]