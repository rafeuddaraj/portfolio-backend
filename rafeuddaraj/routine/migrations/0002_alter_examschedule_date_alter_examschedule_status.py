# Generated by Django 5.0 on 2023-12-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examschedule',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='examschedule',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'InProgress'), (3, 'Complete')], default=1),
        ),
    ]