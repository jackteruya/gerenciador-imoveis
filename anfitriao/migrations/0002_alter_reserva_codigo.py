# Generated by Django 3.2.8 on 2021-10-27 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anfitriao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='codigo',
            field=models.CharField(auto_created=True, default='KLyrosD7vK', editable=False, max_length=10, unique=True),
        ),
    ]
