# Generated by Django 5.0.2 on 2024-03-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uplink', '0003_remove_link_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='order',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
