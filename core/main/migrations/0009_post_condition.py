# Generated by Django 4.0.5 on 2022-07-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='condition',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Used', 'Used')], max_length=100),
        ),
    ]