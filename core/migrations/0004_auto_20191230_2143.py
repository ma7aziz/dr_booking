# Generated by Django 3.0.1 on 2019-12-30 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191230_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='Featured',
            new_name='featured',
        ),
    ]
