# Generated by Django 2.1.2 on 2019-01-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='points_available',
            field=models.BooleanField(default=False, verbose_name='Points Available'),
        ),
    ]
