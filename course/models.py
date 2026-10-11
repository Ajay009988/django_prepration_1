from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=70)
    work=models.CharField(max_length=70)
    state=models.CharField(max_length=79)
    mobile=models.CharField(max_length=70)
    salary=models.IntegerField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name=models.CharField(max_length=80)
    location=models.CharField(max_length=70)
    product=models.CharField(max_length=70)


    def __str__(self):
        return self.name

