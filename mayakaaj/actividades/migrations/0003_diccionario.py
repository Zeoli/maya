# Generated by Django 2.0.2 on 2018-11-07 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_auto_20181106_2353'),
        ('actividades', '0002_auto_20181106_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='diccionario',
            fields=[
                ('idDiccionario', models.AutoField(primary_key=True, serialize=False)),
                ('palabra', models.CharField(max_length=50, verbose_name='Palabra')),
                ('traduccion', models.CharField(max_length=50, verbose_name='Traduccion')),
                ('imagen', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('idLeccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.leccion', verbose_name='Leccion')),
            ],
            options={
                'verbose_name_plural': 'diccionarios',
            },
        ),
    ]