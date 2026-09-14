from django.contrib import admin
from .models import Employee

# นำ Employee ไปแสดงในหน้า Admin
admin.site.register(Employee)