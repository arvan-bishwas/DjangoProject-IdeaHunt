# Generated by Django 2.1.2 on 2018-10-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_auto_20181012_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='idea',
            name='url',
            field=models.TextField(max_length=256),
        ),
    ]
