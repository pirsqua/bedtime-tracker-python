# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bedtime(models.Model):
    bedtime_id = models.AutoField(db_column='BedtimeId', primary_key=True)
    child = models.ForeignKey('Child', on_delete=models.DO_NOTHING, db_column='ChildId')
    sleep_start = models.DateTimeField(db_column='SleepStart')
    sleep_end = models.DateTimeField(db_column='SleepEnd')
    success = models.BooleanField(db_column='Success')
    is_nap = models.BooleanField(db_column='IsNap')

    class Meta:
        managed = False
        db_table = 'Bedtime'


class Child(models.Model):
    child_id = models.AutoField(db_column='ChildId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Child'


class Prize(models.Model):
    prize_id = models.AutoField(db_column='PrizeId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.CharField(db_column='Description', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    image_url = models.CharField(db_column='ImageUrl', max_length=2048, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Prize'
