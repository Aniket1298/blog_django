# Generated by Django 2.0.8 on 2019-07-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190708_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.IntegerField(),
        ),
    ]
