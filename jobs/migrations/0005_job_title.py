# Generated by Django 2.1 on 2018-09-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20180511_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default=False, max_length=100),
        ),
    ]