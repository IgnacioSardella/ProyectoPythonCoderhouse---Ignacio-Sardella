# Generated by Django 4.2.3 on 2023-08-16 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0003_carrera_id_alter_carrera_comision'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alumno',
            new_name='Estudiante',
        ),
    ]
