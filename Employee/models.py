from django.db import models

# Create your models here.

class Employee( models.Model):
    """
    Represents an Employee
    """

    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Department = models.CharField(max_length=20)
    Salary = models.IntegerField(default = 0)