# Generated by Django 4.2.3 on 2023-08-20 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
