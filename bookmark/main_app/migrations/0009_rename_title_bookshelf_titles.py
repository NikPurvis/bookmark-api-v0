# Generated by Django 4.0.4 on 2022-04-26 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_bookshelf_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookshelf',
            old_name='title',
            new_name='titles',
        ),
    ]
