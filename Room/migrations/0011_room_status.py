# Generated by Django 3.1.1 on 2021-01-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0010_auto_20210111_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(default='Enable', max_length=200, null=True),
        ),
    ]
