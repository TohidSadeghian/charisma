# Generated by Django 4.1 on 2022-08-20 00:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_At')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='Is_Deleted')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='price')),
                ('is_fragile', models.BooleanField(default=False, verbose_name='is_fragile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_At')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='Is_Deleted')),
                ('profit', models.DecimalField(decimal_places=4, default=0, max_digits=12, verbose_name='profit')),
                ('percentageـdiscount', models.IntegerField(default=0, verbose_name='percentageـdiscount')),
                ('amountـdiscount', models.DecimalField(decimal_places=4, default=0, max_digits=12, verbose_name='amountـdiscount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_coupons', to='products.product', verbose_name='product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
