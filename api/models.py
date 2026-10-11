from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=80)
    subject=models.CharField(max_length=70)
    city=models.CharField(max_length=70)


    def __str__(self):
        return self.name


class Teacher(models.Model):
    T_name=models.CharField(max_length=80)
    T_course=models.CharField(max_length=80)
    T_location=models.CharField(max_length=80)
    T_email=models.EmailField()
    T_salary=models.IntegerField()

    def __str__(self):
        return self.T_name