# Generated by Django 2.2.3 on 2019-08-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropa',
            name='talla',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=1),
        ),
    ]
