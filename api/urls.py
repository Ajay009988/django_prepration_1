from django.urls import path,include
from . import views


from rest_framework . routers import DefaultRouter


router=DefaultRouter()
router.register(r'student',views.Student,basename='student')
router.register(r'teacher',views.Teacher,basename='teacher')


urlpatterns=[
    path('ho/',views.ho),
    path('',include(router.urls)),
]
