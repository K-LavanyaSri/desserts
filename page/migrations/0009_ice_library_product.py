# Generated by Django 5.1.3 on 2025-02-05 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ice_library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('badge', models.TextField()),
                ('rating', models.IntegerField()),
                ('price', models.IntegerField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='page.ice_library')),
            ],
        ),
    ]
