# Generated by Django 5.1.2 on 2024-11-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='dob',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='result',
            name='dor',
            field=models.TextField(),
        ),
    ]