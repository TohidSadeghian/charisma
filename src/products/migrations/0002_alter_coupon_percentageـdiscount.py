# Generated by Django 4.1 on 2022-08-20 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='percentageـdiscount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12, verbose_name='percentageـdiscoun'),
        ),
    ]
