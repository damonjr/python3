# Generated by Django 4.2.5 on 2023-11-21 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_app', '0002_alter_air_track_hbl_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LmsUser',
        ),
        migrations.AlterModelOptions(
            name='air_orders',
            options={'managed': True},
        ),
        migrations.RemoveField(
            model_name='air_orders',
            name='crate_date',
        ),
        migrations.RemoveField(
            model_name='air_track',
            name='crate_date',
        ),
        migrations.RemoveField(
            model_name='big_ticket',
            name='btg_cket_status',
        ),
        migrations.AddField(
            model_name='air_orders',
            name='create_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='创建日期'),
        ),
        migrations.AddField(
            model_name='air_orders',
            name='hbl_creator',
            field=models.CharField(max_length=100, null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='air_track',
            name='happen_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='发生日期'),
        ),
        migrations.AddField(
            model_name='air_track',
            name='update_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='最后更新日期'),
        ),
        migrations.AddField(
            model_name='air_track',
            name='updater',
            field=models.CharField(max_length=100, null=True, verbose_name='最后修改人'),
        ),
        migrations.AddField(
            model_name='big_ticket',
            name='big_ticket_creator',
            field=models.CharField(max_length=100, null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='big_ticket',
            name='big_ticket_status',
            field=models.CharField(max_length=2, null=True, verbose_name='HBL状态'),
        ),
        migrations.AlterField(
            model_name='air_orders',
            name='big_ticket_id',
            field=models.IntegerField(null=True, verbose_name='大票ID'),
        ),
        migrations.AlterField(
            model_name='air_orders',
            name='hbl_num',
            field=models.CharField(db_index=True, max_length=64, null=True, verbose_name='HBL号'),
        ),
        migrations.AlterField(
            model_name='air_orders',
            name='hbl_remake',
            field=models.CharField(max_length=200, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='air_orders',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='小票id'),
        ),
        migrations.AlterField(
            model_name='air_track',
            name='hbl_id',
            field=models.CharField(default=2, max_length=64, verbose_name='HBL号Id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='air_track',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='小票id'),
        ),
        migrations.AlterField(
            model_name='air_track',
            name='track_remake',
            field=models.CharField(max_length=200, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='big_ticket',
            name='big_ticket_num',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='大票号'),
        ),
        migrations.AlterField(
            model_name='big_ticket',
            name='crate_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='big_ticket',
            name='hbl_remake',
            field=models.CharField(max_length=200, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='big_ticket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='大票id'),
        ),
        migrations.AlterModelTable(
            name='air_orders',
            table='air_app_air_orders',
        ),
    ]