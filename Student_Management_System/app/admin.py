from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Stuff)
admin.site.register(Stuff_Notification)
admin.site.register(Stuff_Leave)
admin.site.register(Stuff_Feedback)
admin.site.register(Student_Notification)
admin.site.register(Student_Result)
admin.site.register(Semester)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)

