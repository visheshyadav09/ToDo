# Generated by Django 3.0.7 on 2020-08-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
