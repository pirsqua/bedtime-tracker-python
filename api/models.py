# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bedtime(models.Model):
    bedtimedate = models.DateField(db_column='BedtimeDate', primary_key=True)  # Field name made lowercase.
    success = models.BooleanField(db_column='Success')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bedtime'


class Prize(models.Model):
    prizeid = models.AutoField(db_column='PrizeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=2048, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prize'
