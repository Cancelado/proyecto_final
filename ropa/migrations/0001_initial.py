# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('propietario', models.CharField(max_length=125)),
                ('telefono', models.IntegerField(default=0)),
                ('mail', models.EmailField(max_length=60, verbose_name=b'E-mail')),
                ('fechaRecibo', models.DateField(verbose_name=b'Fecha de ingreso')),
                ('fechaEntrega', models.DateField(verbose_name=b'Fecha de entrega')),
                ('costo', models.FloatField(default=0)),
                ('color', models.ForeignKey(to='ropa.Color')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPrenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoPrenda', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoTela', models.CharField(max_length=65)),
            ],
        ),
        migrations.AddField(
            model_name='ropa',
            name='tipoPrenda',
            field=models.ForeignKey(to='ropa.TipoPrenda'),
        ),
        migrations.AddField(
            model_name='ropa',
            name='tipoTela',
            field=models.ForeignKey(to='ropa.TipoTela'),
        ),
    ]
