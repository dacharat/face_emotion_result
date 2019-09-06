# Generated by Django 2.2.3 on 2019-07-30 08:31

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0011_testperson_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testperson',
            name='record',
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recoed_name', models.CharField(max_length=200)),
                ('emotion_detail', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.TestPerson')),
            ],
            options={
                'db_table': 'record',
                'managed': True,
            },
        ),
    ]
