# Generated by Django 2.2.5 on 2020-03-10 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0018_destination_liked'),
        ('post', '0003_auto_20200308_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinations.Destination'),
        ),
    ]
