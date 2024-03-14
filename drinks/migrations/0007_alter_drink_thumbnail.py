# Generated by Django 5.0 on 2024-02-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0006_drink_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/drink_images/default.png', null=True, upload_to='drink_images/'),
        ),
    ]