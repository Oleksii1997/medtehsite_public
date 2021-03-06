# Generated by Django 3.0.4 on 2020-03-23 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200322_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorygoods',
            name='category_image',
            field=models.ImageField(default=0, upload_to='stylesheet/media/category_product_image/'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='is_main_image',
            field=models.BooleanField(default=False),
        ),
    ]
