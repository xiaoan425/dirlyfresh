# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=10)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=20)),
                ('ureceiver', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100)),
                ('upostcode', models.IntegerField(max_length=6)),
                ('uphone', models.IntegerField(max_length=11)),
            ],
        ),
    ]
