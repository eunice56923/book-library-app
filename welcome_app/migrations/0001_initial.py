# Generated by Django 5.1.2 on 2024-11-11 12:01

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.CharField(default='No description provided', max_length=255)),
                ('publish_date', models.DateField(default=datetime.date.today)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='book_pdfs/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='welcome_app.category')),
            ],
        ),
    ]