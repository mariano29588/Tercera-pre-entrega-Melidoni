# Generated by Django 4.2.2 on 2023-08-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_remove_estudiantes_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='estudiantes/'),
        ),
    ]
