# Generated by Django 4.1.3 on 2022-12-07 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_groupfinder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupfinder',
            name='user',
        ),
        migrations.AddField(
            model_name='groupfinder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
