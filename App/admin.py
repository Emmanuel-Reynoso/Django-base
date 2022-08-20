from django.contrib import admin
from App.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'occupation', 'salary', 'gender', 'created_at']
    search_fields = ['name', 'email', 'occupation', 'salary']
    list_filter = ['gender']
    list_per_page = 8

admin.site.register(Employee, EmployeeAdmin)

