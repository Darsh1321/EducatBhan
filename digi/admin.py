from django.contrib import admin
from .models import Student,Professor,Classes_taught,AssgProfessor,AssgStudent
# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Classes_taught)
admin.site.register(AssgProfessor)
admin.site.register(AssgStudent)