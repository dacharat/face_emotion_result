# Generated by Django 2.2.2 on 2019-07-12 10:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0004_auto_20190628_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='testperson',
            name='face_encodong',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=[], size=None),
        ),
    ]