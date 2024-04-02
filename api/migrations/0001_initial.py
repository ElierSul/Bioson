# Generated by Django 5.0.3 on 2024-04-01 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_departamento', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEtiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPermiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('contrasena', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_municipio', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=45)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.departamento')),
            ],
            options={
                'unique_together': {('codigo_municipio', 'departamento')},
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=200)),
                ('tasa_muestreo', models.CharField(max_length=45)),
                ('rango_frecuencias', models.CharField(max_length=45)),
                ('tipo_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipoequipo')),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=200)),
                ('tipo_etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipoetiqueta')),
            ],
            options={
                'unique_together': {('id', 'tipo_etiqueta')},
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitud', models.CharField(max_length=45)),
                ('latitud', models.CharField(max_length=45)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=200)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_archivo', models.CharField(max_length=50)),
                ('ruta', models.CharField(max_length=45)),
                ('fecha_creacion', models.DateField()),
                ('creador', models.CharField(max_length=45)),
                ('coleccion', models.ManyToManyField(db_table='coleccion_audio', to='api.coleccion')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipo')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ubicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Anotacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_inicio', models.TimeField()),
                ('tiempo_final', models.TimeField()),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.audio')),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.etiqueta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioPermiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipopermiso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_permiso',
            field=models.ManyToManyField(through='api.UsuarioPermiso', to='api.tipopermiso'),
        ),
        migrations.AddField(
            model_name='coleccion',
            name='coleccion_compartida',
            field=models.ManyToManyField(db_table='coleccion_compartida', to='api.usuariopermiso'),
        ),
    ]