# Generated by Django 2.1.2 on 2018-10-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20181012_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='url',
            field=models.TextField(),
        ),
    ]
