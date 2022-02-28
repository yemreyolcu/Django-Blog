from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('todo/',views.showtodo,name="showtodo"),
    path('create/',views.createtodo,name="createtodo"),
    path('delete/<int:id>',views.deltodo,name="deltodo"),
    path('update/<int:id>',views.updatetodo,name="upttodo"),


]