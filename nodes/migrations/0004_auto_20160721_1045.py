# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0003_auto_20160720_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='node_id',
            field=models.CharField(max_length=255),
        ),
    ]
