# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-12 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_brand', models.CharField(max_length=100)),
                ('btitle', models.CharField(max_length=30)),
                ('isdelete', models.IntegerField(db_column='isDelete')),
            ],
            options={
                'db_table': 'Brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Carinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=30)),
                ('regist_date', models.DateField()),
                ('engineno', models.CharField(db_column='engineNo', max_length=30)),
                ('mileage', models.IntegerField()),
                ('maintenance_record', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('extractprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('newprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('picture', models.CharField(max_length=100)),
                ('formalities', models.CharField(max_length=10)),
                ('debt', models.CharField(max_length=10)),
                ('promise', models.TextField(blank=True, null=True)),
                ('examine', models.CharField(max_length=30)),
                ('ispurchase', models.IntegerField(db_column='isPurchase')),
                ('isdelete', models.IntegerField(db_column='isDelete')),
            ],
            options={
                'db_table': 'Carinfo',
                'managed': False,
            },
        ),
    ]
