# Generated by Django 4.1.1 on 2022-09-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Book title')),
                ('description', models.TextField(verbose_name='Book description')),
                ('date_published', models.DateField(auto_now_add=True)),
                ('isbn', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('genre', models.CharField(choices=[('COMEDY', 'comedy'), ('TRAGEDY', 'tragedy'), ('FICTION', 'fiction'), ('NON_FICTION', 'non_fiction'), ('ROMANCE', 'romance')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('number', models.PositiveSmallIntegerField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(default='Lagos', max_length=255)),
                ('country', models.CharField(default='Nigeria', max_length=255)),
                ('publisher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('A', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='my_app.publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='authors', through='my_app.BookAuthor', to='my_app.book'),
        ),
    ]
