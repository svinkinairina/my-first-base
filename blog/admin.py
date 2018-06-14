from django.contrib import admin
from .models import Specalty
from .models import Group
from .models import Student
from .models import Teacher
from .models import Subject
from .models import Journal

admin.site.register(Specalty)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Journal)