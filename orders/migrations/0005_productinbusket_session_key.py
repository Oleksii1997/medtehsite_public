# Generated by Django 3.0.4 on 2020-04-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_productinbusket'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbusket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
