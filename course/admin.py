from django.contrib import admin
from . models import Employee , Company

@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','work','state','mobile','salary']

@admin.register(Company)

class CompanyAdmin(admin.ModelAdmin):
    list_display=['id','name','location','product']