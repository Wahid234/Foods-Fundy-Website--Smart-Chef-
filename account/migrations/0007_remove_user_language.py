# Generated by Django 5.0.2 on 2024-03-15 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_devices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='language',
        ),
    ]
