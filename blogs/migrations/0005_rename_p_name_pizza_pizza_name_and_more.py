# Generated by Django 4.0.4 on 2022-05-27 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_a_name_artist_artist_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='p_name',
            new_name='pizza_name',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='toppings',
            new_name='toppings_name',
        ),
        migrations.RenameField(
            model_name='toppings',
            old_name='t_name',
            new_name='toppings_name',
        ),
    ]