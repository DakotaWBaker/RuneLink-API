# Generated by Django 4.1.3 on 2022-11-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rsn',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
