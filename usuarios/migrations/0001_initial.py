# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=65)),
                ('apellidos', models.CharField(max_length=125)),
                ('fecha', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('edad', models.IntegerField(default=0)),
                ('mail', models.EmailField(max_length=60, verbose_name=b'E-mail')),
            ],
        ),
    ]
