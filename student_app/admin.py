from django.contrib import admin

# Register your models here.
from student_app.models import Student,Note
admin.site.register(Student)
admin.site.register(Note)

