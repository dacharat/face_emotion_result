# Generated by Django 2.2.3 on 2019-07-30 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0013_auto_20190730_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='recoed_name',
            new_name='record_name',
        ),
    ]