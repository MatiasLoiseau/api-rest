# Generated by Django 2.0 on 2017-12-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimiento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='descripcion',
            field=models.CharField(default='operacion compra-venta', max_length=200),
        ),
    ]