# Generated by Django 2.0.2 on 2018-05-11 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='image',
            new_name='imagefun',
        ),
    ]
