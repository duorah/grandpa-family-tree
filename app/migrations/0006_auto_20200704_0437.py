# Generated by Django 3.0.7 on 2020-07-04 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200704_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='social',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='person',
            name='origin',
            field=models.CharField(choices=[('P', 'Patrilineal'), ('I', 'Inherited'), ('M', 'Matrilineal'), ('T', 'Taken')], max_length=2),
        ),
    ]
