from django.contrib import admin
from django.urls import path
from myapp import views
app_name='myapp'

urlpatterns = [
    path('sample2/<data>',views.sample2,name='sample2'),
    path('sample3/',views.sample3,name='sample3'),
]
