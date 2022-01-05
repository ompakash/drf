from django.contrib import admin
from api.models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','mobile','roll','city']
