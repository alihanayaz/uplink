# Generated by Django 5.0.2 on 2024-03-10 19:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uplink', '0002_customuser_groups_customuser_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must contain only alphanumeric characters.', regex='^[a-zA-Z0-9]+$')]),
        ),
    ]