from django.contrib import admin
from .models import CustomUser, Session, Course, Department
# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'has_type', 'tutor', 'student', 'name')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'course', 'experience', 'hourly_rate', 'location', 'start_time', 'end_time', 'day', 'availability')

class DepartmentAdmin(admin.ModelAdmin):
    list_display= ('dept_name', 'dept_mnemonic')
admin.site.register(CustomUser)
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(Department)
