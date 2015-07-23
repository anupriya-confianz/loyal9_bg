# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(default='', max_length=20)),
                ('Company', models.CharField(default='', max_length=50)),
                ('CrmId', models.IntegerField(default=0)),
                ('PhoneNumber', models.CharField(default='', max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ContactId', models.IntegerField(default=0)),
                ('TotalPaid', models.CharField(default='', max_length=10)),
                ('TotalDue', models.CharField(default='', max_length=10)),
                ('InvoiceId', models.IntegerField(default=0)),
                ('InvoiceTotal', models.CharField(default='', max_length=35)),
                ('RefundStatus', models.CharField(default='', max_length=35)),
                ('DateCreated', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ItemOrderId', models.IntegerField(default=0)),
                ('InvoiceId', models.IntegerField(default=0)),
                ('OrderItemId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OrderId', models.IntegerField(default=0)),
                ('ProductId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PaymentId', models.CharField(default=0, max_length=35)),
                ('UserId', models.IntegerField(default=0)),
                ('InvoiceId', models.IntegerField(default=0)),
                ('PayAmt', models.CharField(default='', max_length=35)),
            ],
        ),
    ]
