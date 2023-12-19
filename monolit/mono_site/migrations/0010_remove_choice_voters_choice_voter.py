# Generated by Django 4.2.8 on 2023-12-19 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mono_site', '0009_choice_voters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='voters',
        ),
        migrations.AddField(
            model_name='choice',
            name='voter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
