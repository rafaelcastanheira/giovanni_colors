# Generated by Django 3.1.5 on 2021-01-25 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210125_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.IntegerField(choices=[(1, 'Street'), (2, 'Canvas'), (3, 'Design')], default=1),
        ),
    ]
