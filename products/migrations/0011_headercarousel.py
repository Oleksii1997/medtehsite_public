# Generated by Django 3.0.4 on 2020-07-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200329_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='stylesheet/media/homepage_carousel/')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Фото каруселі',
                'verbose_name_plural': 'Фото каруселі',
            },
        ),
    ]
