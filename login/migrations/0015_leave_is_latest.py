# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='is_latest',
            field=models.BooleanField(default=True),
        ),
    ]
