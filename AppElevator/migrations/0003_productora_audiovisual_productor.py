# Generated by Django 4.2.4 on 2023-09-27 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppElevator', '0002_proyecto_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='productora_audiovisual',
            name='Productor',
            field=models.ManyToManyField(to='AppElevator.productor'),
        ),
    ]
