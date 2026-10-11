from django.shortcuts import render
from django.http import HttpResponse


def api(request):
    return HttpResponse("this is a course page")


from . models import Employee
from . models import Company
from . serializers import EmployeeSerializer
from . serializers import CompanySerializer
from rest_framework  import viewsets


class Employee(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


class Company(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer