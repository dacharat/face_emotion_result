# Generated by Django 2.2.2 on 2019-07-12 10:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0006_auto_20190712_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testperson',
            name='face_encodong',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default={}, size=None),
        ),
    ]