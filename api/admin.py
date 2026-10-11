from django.contrib import admin
from . models import Teacher,Student


@admin.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','T_name','T_course','T_location','T_email','T_salary']
    search_fields=['T_name']


@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','subject','city']
    search_fields=['name']