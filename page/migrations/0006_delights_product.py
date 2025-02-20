# Generated by Django 5.1.3 on 2025-02-01 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_delete_delights'),
    ]

    operations = [
        migrations.CreateModel(
            name='delights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField()),
                ('badge', models.TextField()),
                ('discription', models.TextField()),
                ('rating', models.IntegerField()),
                ('price', models.IntegerField()),
                ('library', models.TextField()),
            ],
        ),
    ]
