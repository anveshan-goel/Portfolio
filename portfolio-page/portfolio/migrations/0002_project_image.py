# Generated by Django 4.0 on 2021-12-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
    ]