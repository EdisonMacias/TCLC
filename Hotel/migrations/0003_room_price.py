# Generated by Django 4.0.5 on 2023-01-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0002_remove_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Precio'),
            preserve_default=False,
        ),
    ]
