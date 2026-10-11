from django.shortcuts import render
from django.http import HttpResponse


def ho(request):
    return HttpResponse("this is a api page")


from . models import Student
# from rest_framework . viewsets import ModelViewSet
from rest_framework import viewsets
from . serializers import StudentSerializer
from . serializers import TeacherSerializer
from . models import Teacher


class Student(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class Teacher(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    