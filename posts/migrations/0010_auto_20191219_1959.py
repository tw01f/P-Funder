# Generated by Django 2.2.7 on 2019-12-19 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20191219_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bankAccount',
            field=models.CharField(blank=True, help_text='This is for Jazzcash / EasyPaisa / Bank money transfer', max_length=26, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cnic',
            field=models.IntegerField(blank=True, help_text='This is for Jazzcash / EasyPaisa money transfer', null=True, validators=[django.core.validators.MaxValueValidator(11111111111111111111111111)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='mobileAccount',
            field=models.CharField(blank=True, help_text='Enter your Jazzcash or EasyPaisa Account\nThis is for Jazzcash or EasyPaisa money transfer', max_length=15, null=True),
        ),
    ]