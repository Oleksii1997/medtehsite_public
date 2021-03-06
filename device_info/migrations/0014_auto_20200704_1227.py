# Generated by Django 3.0.4 on 2020-07-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0013_repairdevice_pay_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairdevice',
            name='add_comment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='repairdevice',
            name='start_warranty',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='repairdevice',
            name='stop_warranty',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
