# Generated by Django 2.2.28 on 2022-05-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220514_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='image_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='image_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(height_field='image_heigth', upload_to='uploads/', width_field='image_width'),
        ),
    ]