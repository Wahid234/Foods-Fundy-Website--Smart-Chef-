# Generated by Django 5.0.2 on 2024-03-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0007_remove_usermealingredient_meals_usermeals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermealingredient',
            name='devices',
            field=models.ManyToManyField(blank=True, related_name='umi_devices', to='meal.device', verbose_name='Devices'),
        ),
        migrations.AlterField(
            model_name='usermealingredient',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='umi_tags', to='meal.tag', verbose_name='Tags'),
        ),
    ]
