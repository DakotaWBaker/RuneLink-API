# Generated by Django 4.1.3 on 2022-12-06 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_skilllevels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skilllevels',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.skilllevels'),
        ),
    ]