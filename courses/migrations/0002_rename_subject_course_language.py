# Generated by Django 4.2.1 on 2023-05-30 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='subject',
            new_name='language',
        ),
    ]
