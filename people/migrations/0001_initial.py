# Generated by Django 3.2.10 on 2022-01-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('about', models.TextField()),
            ],
        ),
    ]