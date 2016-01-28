# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteT', '0009_cliente_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='dataNascimento',
            new_name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='CPF',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default=b'blank', max_length=11),
        ),
    ]
