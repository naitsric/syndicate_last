# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount_discount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]