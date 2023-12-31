# Generated by Django 4.2.3 on 2023-08-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_speaker_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/Speakers'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(upload_to='media/Sponsors'),
        ),
    ]
