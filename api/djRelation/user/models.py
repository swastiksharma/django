from django.db import models


class users(models.Model):
    First_name = models.TextField(max_length=100)
    last= models.TextField(max_length=100)
    email = models.EmailField()
    mobile = models.TextField(max_length=100)
class Customer(models.Model):
    Profile_no = models.TextField(max_length=100)

