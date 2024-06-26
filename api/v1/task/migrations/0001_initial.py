# Generated by Django 5.0.3 on 2024-04-18 06:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to='files/')),
                ('group', models.CharField(choices=[('Media', 'Media'), ('Docs', 'Docs'), ('Videos', 'Videos')], default='Docs', max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_files', to=settings.AUTH_USER_MODEL)),
                ('sharing', models.ManyToManyField(blank=True, related_name='sharing_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
