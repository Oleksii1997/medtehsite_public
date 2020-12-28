# Generated by Django 3.0.4 on 2020-04-27 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_type', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Тип листа: ',
                'verbose_name_plural': 'Типи листів',
            },
        ),
        migrations.CreateModel(
            name='EmailSending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_sending.EmailType')),
            ],
            options={
                'verbose_name': 'Відправлений лист: ',
                'verbose_name_plural': 'Відправлені листи',
            },
        ),
    ]
