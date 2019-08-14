# Generated by Django 2.2.3 on 2019-08-14 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('nit', models.TextField(blank=True, default='C/F')),
                ('direccion', models.TextField(blank=True, default='Ciudad')),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRopa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estilo', models.TextField()),
                ('talla', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('color', models.TextField()),
                ('precio', models.FloatField()),
                ('Tipo_ropa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplicacion.TipoRopa')),
            ],
            options={
                'verbose_name': 'Ropa',
                'verbose_name_plural': 'Ropas',
            },
        ),
        migrations.CreateModel(
            name='OrdenDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplicacion.Orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplicacion.Ropa')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='producto',
            field=models.ManyToManyField(through='Aplicacion.OrdenDetalle', to='Aplicacion.Ropa'),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=12)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('pago', models.CharField(choices=[('efectivo', 'efectivo'), ('tarjeta', 'tarjeta'), ('ccuponu', 'cupon')], max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplicacion.Cliente')),
                ('orden', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.Orden')),
            ],
        ),
    ]
