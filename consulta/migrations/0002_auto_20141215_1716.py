# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Beneficiario',
            new_name='Localizar_CPF',
        ),
    ]
