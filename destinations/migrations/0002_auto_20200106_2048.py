# Generated by Django 2.2.5 on 2020-01-06 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='city',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country'),
        ),
    ]
