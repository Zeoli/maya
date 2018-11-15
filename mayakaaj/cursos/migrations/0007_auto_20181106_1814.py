# Generated by Django 2.0.2 on 2018-11-07 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_auto_20181105_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diccionario',
            name='significado',
        ),
        migrations.AddField(
            model_name='diccionario',
            name='traduccion',
            field=models.CharField(default='as', max_length=50, verbose_name='Traduccion'),
            preserve_default=False,
        ),
    ]