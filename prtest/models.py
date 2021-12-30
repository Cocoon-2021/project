from django.db import models


class Details(models.Model):
    name = models.CharField(max_length=20, default='', null=False)
    email = models.CharField(max_length=30, default='', null=False)
    gender = models.CharField(max_length=20, default='', null=False)
    num = models.CharField(max_length=20, default='', null=False)
    dob = models.CharField(max_length=20, default='', null=False)
    pname = models.CharField(max_length=20, default='', null=False)
    pnum = models.CharField(max_length=20, default='', null=False)
    passwd = models.CharField(max_length=20, default='', null=False)
# Create your models here.
