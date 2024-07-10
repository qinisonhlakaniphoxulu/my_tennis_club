from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True) #phone
    joined_date = models.DateField(null=True) #joined_date

