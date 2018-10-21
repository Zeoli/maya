# Generated by Django 2.0.2 on 2018-10-16 00:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('idCurso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('fechaInicioCurso', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Inicio')),
                ('fechaFinalCurso', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Fin')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
        migrations.CreateModel(
            name='leccion',
            fields=[
                ('idLeccion', models.AutoField(primary_key=True, serialize=False)),
                ('tema', models.CharField(max_length=80)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'lecciones',
            },
        ),
        migrations.CreateModel(
            name='unidad',
            fields=[
                ('idUnidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
            ],
            options={
                'verbose_name_plural': 'unidades',
            },
        ),
        migrations.AddField(
            model_name='leccion',
            name='idUnidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.unidad'),
        ),
    ]