# Generated by Django 4.2.3 on 2023-08-16 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0004_rename_alumno_estudiante'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'ordering': ['id']},
        ),
    ]
