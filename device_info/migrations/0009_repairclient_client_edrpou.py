# Generated by Django 3.0.4 on 2020-05-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0008_auto_20200524_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairclient',
            name='client_edrpou',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
    ]