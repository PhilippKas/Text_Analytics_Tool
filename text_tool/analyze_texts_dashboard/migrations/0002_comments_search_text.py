# Generated by Django 5.0.2 on 2024-02-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze_texts_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='search_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
