# Generated by Django 3.1.2 on 2020-11-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='comments',
            field=models.CharField(default='comments has not been added', max_length=512),
        ),
        migrations.AlterField(
            model_name='method',
            name='command',
            field=models.CharField(default='df -h', max_length=512),
        ),
    ]
