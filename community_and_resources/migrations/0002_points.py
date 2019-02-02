# Generated by Django 2.1.2 on 2019-02-02 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community_and_resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255, verbose_name='Event Name')),
                ('report_time', models.TimeField(verbose_name='Event Time')),
                ('first_east', models.FloatField(verbose_name='1st East')),
                ('first_west', models.FloatField(verbose_name='1st West')),
                ('second_east', models.FloatField(verbose_name='2nd East')),
                ('second_west', models.FloatField(verbose_name='2nd West')),
                ('third_east', models.FloatField(verbose_name='3rd East')),
                ('third_west', models.FloatField(verbose_name='3rd West')),
                ('fourth_east', models.FloatField(verbose_name='4th East')),
                ('fourth_west', models.FloatField(verbose_name='4th West')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]