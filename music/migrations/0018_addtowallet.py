# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0017_auto_20170331_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default=0, max_length=20)),
                ('currency', models.CharField(default='usd', max_length=5)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
