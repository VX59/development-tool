# Generated by Django 4.1.4 on 2023-01-06 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtrack', '0012_sprint_active_alter_sprint_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 21, 38, 35, 434321, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 21, 38, 35, 434321, tzinfo=datetime.timezone.utc)),
        ),
    ]