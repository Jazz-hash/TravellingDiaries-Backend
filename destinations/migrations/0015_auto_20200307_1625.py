# Generated by Django 2.2.5 on 2020-03-07 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0018_remove_review_destination'),
        ('destinations', '0014_auto_20200307_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinationimage',
            name='destination',
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.DeleteModel(
            name='DestinationImage',
        ),
    ]
