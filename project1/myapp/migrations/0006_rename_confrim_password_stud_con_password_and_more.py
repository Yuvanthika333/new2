# Generated by Django 5.0.6 on 2024-06-24 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_con_password_stud_confrim_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud',
            old_name='confrim_password',
            new_name='con_password',
        ),
        migrations.RenameField(
            model_name='stud',
            old_name='stud_c',
            new_name='student_c',
        ),
    ]
