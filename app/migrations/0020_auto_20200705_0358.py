# Generated by Django 3.0.7 on 2020-07-05 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200705_0354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='givenname',
            new_name='given_name',
        ),
    ]
