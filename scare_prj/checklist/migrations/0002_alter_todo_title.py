# Generated by Django 5.0.7 on 2024-07-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
