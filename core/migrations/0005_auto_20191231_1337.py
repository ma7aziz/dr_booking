# Generated by Django 3.0.1 on 2019-12-31 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191230_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='category',
            new_name='speciality',
        ),
    ]
