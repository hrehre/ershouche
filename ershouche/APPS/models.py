

from django.db import models


class Carinfo(models.Model):
    title = models.CharField(max_length=200)
    trademark = models.CharField(max_length=200)
    car_series = models.CharField(max_length=200)
    original_price = models.CharField(max_length=200)
    current_price = models.CharField(max_length=200)
    car_age = models.CharField(max_length=200)
    car_type = models.CharField(max_length=200)
    seat = models.CharField(max_length=200)
    road_haul = models.CharField(max_length=200)
    gearbox = models.CharField(max_length=200)
    displacement = models.CharField(max_length=200)
    emi_standard = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    collect_num = models.CharField(max_length=200)


class Car_img(models.Model):
    car = models.ForeignKey(Carinfo)
    url = models.CharField(max_length=200)


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    ticket = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=20)
    sex = models.IntegerField(default=0)
    phone_num = models.CharField(max_length=11)
    user_icon = models.CharField(max_length=200)
    classes = models.CharField(max_length=100)
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = 'user'


class Permission(models.Model):

    p_name = models.CharField(max_length=10)
    p_en = models.CharField(max_length=10)

    class Meta:
        db_table = 'permission'


class Role(models.Model):

    r_name = models.CharField(max_length=100)
    u = models.OneToOneField(User, on_delete=models.CASCADE)
    r_p = models.ManyToManyField(Permission)

    class Meta:
        db_table = 'role'


class Collection(models.Model):
    user = models.ForeignKey(User)
    car = models.ForeignKey(Carinfo)