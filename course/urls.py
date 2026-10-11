from django.urls import path,include
from . import views
from rest_framework. routers import DefaultRouter



router=DefaultRouter()
router.register(r'employee',views.Employee,basename='employee')
router.register(r'company',views.Company,basename='company')


urlpatterns=[
    path('ap/',views.api),
    path('',include(router.urls)),
]