# Generated by Django 2.2.4 on 2019-08-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_auto_20190817_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='preparation_time',
            new_name='preperation_time',
        ),
    ]