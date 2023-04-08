# Generated by Django 4.1.4 on 2023-01-04 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devtrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_name', models.CharField(max_length=16)),
                ('calendar_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devtrack.project')),
            ],
        ),
    ]
