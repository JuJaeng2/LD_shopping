# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# < 데이터베이스와 연결된 파일 >

from django.db import models




class Address(models.Model):
    a_code = models.IntegerField(primary_key=True)
    a_address = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'address'


class Cart(models.Model):
    ca_code = models.IntegerField(primary_key=True)
    u_id = models.IntegerField()
    c_code = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cart'


class Cloth(models.Model):
    c_code = models.IntegerField(primary_key=True)
    c_category = models.CharField(max_length=45)
    c_size = models.CharField(max_length=45)
    c_color = models.CharField(max_length=45)
    c_price = models.IntegerField()
    c_countLeft = models.IntegerField()
    c_countBuy = models.IntegerField()
    c_image = models.ImageField(blank=True, upload_to="")

    class Meta:
        managed = False
        db_table = 'cloth'


class Purchase(models.Model):
    p_code = models.IntegerField(primary_key=True)
    c_code = models.IntegerField()
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchase'


class Review(models.Model):
    r_code = models.IntegerField(primary_key=True)
    u_id = models.IntegerField()
    r_title = models.CharField(max_length=45)
    r_content = models.CharField(max_length=100)
    r_star = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'review'


class User(models.Model):
    u_id = models.IntegerField(primary_key=True)
    u_pw = models.IntegerField()
    a_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

class Test(models.Model):
        imagePath = models.ImageField(blank=True, upload_to="")
