# Generated by Django 3.1.2 on 2020-11-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_flow'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
