# Generated by Django 4.1.3 on 2022-12-06 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_customuser_skill_skilllevels_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skilllevels',
            old_name='skill',
            new_name='user',
        ),
    ]
