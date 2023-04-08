# Generated by Django 4.1.4 on 2023-01-06 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtrack', '0009_feature_resolved_feature_sprint_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 21, 8, 56, 711687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 21, 8, 56, 711687, tzinfo=datetime.timezone.utc)),
        ),
    ]
