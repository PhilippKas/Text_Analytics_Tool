# Generated by Django 5.0.2 on 2024-02-25 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyze_texts_dashboard', '0002_comments_search_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='search_text',
        ),
    ]
