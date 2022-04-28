# Generated by Django 4.0.4 on 2022-04-28 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=13)),
                ('genre', models.CharField(max_length=100)),
                ('olid', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('star_rating', models.PositiveSmallIntegerField(choices=[(0, '0 stars'), (1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])),
                ('have_finished', models.BooleanField(default=False)),
                ('book_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('shelved', models.ManyToManyField(related_name='on_shelf', to='library.book')),
            ],
            options={
                'verbose_name': 'bookshelf',
                'verbose_name_plural': 'bookshelves',
            },
        ),
    ]
