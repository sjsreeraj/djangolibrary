"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views
app_name='books'
urlpatterns = [
    path('',views.home,name="home"),
    path('addbooks',views.addbooks,name="addbooks"),
    path('viewbooks',views.viewbooks,name="viewbooks"),
    path('add1',views.add1,name="add1"),
    path('fact',views.fact,name="fact"),
    path('detail/<int:p>', views.detail, name="detail"),
    path('delete/<int:p>', views.delete, name="delete"),
    path('edit/<int:p>', views.edit, name="edit"),
    path('search',views.search,name="search"),

]
