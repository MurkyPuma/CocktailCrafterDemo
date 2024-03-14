# Generated by Django 5.0 on 2024-02-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_account_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='alcoholic',
        ),
        migrations.RemoveField(
            model_name='account',
            name='category',
        ),
        migrations.RemoveField(
            model_name='account',
            name='glass',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient1',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient2',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient3',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient4',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient5',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient6',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient7',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient8',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ingredient9',
        ),
        migrations.RemoveField(
            model_name='account',
            name='instructions',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement1',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement2',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement3',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement4',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement5',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement6',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement7',
        ),
        migrations.RemoveField(
            model_name='account',
            name='measurement8',
        ),
        migrations.RemoveField(
            model_name='account',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
        migrations.AlterField(
            model_name='account',
            name='favourites',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='recent',
            field=models.BooleanField(default=False),
        ),
    ]