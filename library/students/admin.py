from django.contrib import admin

# Register your models here.
from students.models import student,CustomUser
admin.site.register(student)
admin.site.register(CustomUser)
