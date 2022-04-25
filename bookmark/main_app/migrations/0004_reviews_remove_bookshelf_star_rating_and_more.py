# Generated by Django 4.0.4 on 2022-04-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_book_user_bookshelf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rating', models.PositiveSmallIntegerField(choices=[(0, '0 stars'), (1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')], help_text='How would you rate this book?')),
            ],
        ),
        migrations.RemoveField(
            model_name='bookshelf',
            name='star_rating',
        ),
        migrations.RemoveField(
            model_name='bookshelf',
            name='stars',
        ),
    ]