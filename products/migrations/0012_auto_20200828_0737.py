# Generated by Django 3.0.4 on 2020-08-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_headercarousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Виробник товару: ',
                'verbose_name_plural': 'Виробники товарів',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='compatible_product_brand',
            field=models.ManyToManyField(to='products.BrandProducts'),
        ),
    ]