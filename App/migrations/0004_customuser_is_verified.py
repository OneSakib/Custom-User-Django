# Generated by Django 4.0.6 on 2022-07-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
