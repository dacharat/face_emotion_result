# Generated by Django 2.2.3 on 2019-07-31 11:03

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import graph.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('face', models.CharField(max_length=200)),
                ('emotion_detail', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='TestPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.CharField(max_length=200)),
                ('face_image', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('face_encoding', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=graph.models.array_field_default, size=None)),
            ],
            options={
                'db_table': 'test_person',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_name', models.CharField(max_length=200)),
                ('emotion_detail', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.TestPerson')),
            ],
            options={
                'db_table': 'record',
                'managed': True,
            },
        ),
    ]
