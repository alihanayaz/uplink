# Generated by Django 5.0.2 on 2024-03-05 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uplink', '0002_alter_link_title_alter_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='description',
        ),
    ]
