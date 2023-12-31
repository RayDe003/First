# Generated by Django 4.2.8 on 2023-12-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mono_site', '0005_question_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='full_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='poll_images/'),
        ),
        migrations.AddField(
            model_name='question',
            name='short_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
