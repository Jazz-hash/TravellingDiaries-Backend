# Generated by Django 2.2.5 on 2020-03-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_auto_20200305_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='certificates',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
