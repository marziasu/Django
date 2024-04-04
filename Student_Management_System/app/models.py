from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER=((1, 'HOD'),
          (2,'STAFF'),
          (3,'STUDENT')
    )
    user_type=models.CharField(choices=USER,max_length=58,default=1)
    profile_pic=models.ImageField(upload_to='media/profile_pic')

class Session(models.Model):
    session_start=models.CharField(max_length=100)
    session_end=models.CharField(max_length=100)
    def __str__(self):
        return self.session_start+"To"+self.session_end

class Semester(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    hod_name = models.CharField(max_length=100,default=" ")
    started_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.dept_name
class Student(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    student_rid=models.CharField(max_length=100, null=True)
    gender=models.CharField(max_length=100)
    department_id=models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    semester_id = models.ForeignKey(Semester, on_delete=models.DO_NOTHING,null=True)
    address=models.TextField()
    def __str__(self):
        return self.admin.first_name+" "+self.admin.last_name

class Stuff(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    gender=models.CharField(max_length=100)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.admin.username

class Course(models.Model):
    name=models.CharField(max_length=100)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    semester_id = models.ForeignKey(Semester, on_delete=models.DO_NOTHING,null=True)
    stuff_id = models.ForeignKey(Stuff, on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add='true',null=True)
    updated_at=models.DateTimeField(auto_now='true')
    def __str__(self):
        return self.name

class Stuff_Notification(models.Model):
    stuff_id=models.ForeignKey(Stuff,on_delete=models.CASCADE)
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.stuff_id.admin.first_name+" "+self.stuff_id.admin.last_name

class Stuff_Leave(models.Model):
    stuff_id=models.ForeignKey(Stuff,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    message=models.TextField(null=True)
    mfile=models.FileField(upload_to='media/leave_file',blank=True)
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.stuff_id.admin.first_name+" "+self.stuff_id.admin.last_name

class Stuff_Feedback(models.Model):
    stuff_id=models.ForeignKey(Stuff,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.stuff_id.admin.first_name+" "+self.stuff_id.admin.last_name

class Student_Notification(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    message= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.student_id.admin.first_name+" "+self.student_id.admin.last_name

class Attendance(models.Model)  :
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField()
    semester=models.ForeignKey(Semester,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.attendance_date)

class Attendance_Report(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status = models.IntegerField(null=True, default=0)
    def __str__(self):
        return self.student_id.student_rid

class Student_Result(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    assignment_mark=models.IntegerField()
    exam_mark=models.IntegerField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.student_id.admin.first_name



