# Generated by Django 5.1.6 on 2025-02-19 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_user_todolist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='hora',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AddField(
            model_name='todolist',
            name='dia',
            field=models.DateField(default=datetime.date(2025, 2, 19)),
        ),
    ]
