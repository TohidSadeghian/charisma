# Generated by Django 4.1 on 2022-08-20 00:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_At')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='Is_Deleted')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
