from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Student_Notification, Student, Student_Result, Course, Attendance, Attendance_Report
from django.contrib import messages

def HOME(request):
    return render(request,'Student/home.html')


def STUDENT_RE_NOTIFICATION(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id=student_id)
        context = {
            'notification': notification,
        }
        return render(request, 'Student/notification.html', context)


def MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_re_notification')


def STUDENT_VIEW_RESULT(request):
    student = Student.objects.get(admin=request.user.id)
    result = Student_Result.objects.filter(student_id=student)
    context = {
        'result': result,
    }
    return render(request, 'Student/view_result.html', context)


def STUDENT_VIEW_ATTENDANCE(request):
    student_id=Student.objects.get(admin=request.user.id)
    semester=student_id.semester_id
    course=Course.objects.filter(semester_id=semester)
    action = request.GET.get('action')
    get_course=None
    attendance_report=None
    total_present=0
    total_class=0
    if action is not None:
        if request.method == "POST":
            course_id=request.POST.get('course_id')
            get_course=Course.objects.get(id=course_id)
            total_class=Attendance.objects.filter(course_id=get_course).count()
            attendance_report=Attendance_Report.objects.filter(student_id=student_id, attendance_id__course_id=get_course )
            total_present=Attendance_Report.objects.filter(student_id=student_id, attendance_id__course_id=get_course ).count()

    context={
        'course': course,
        'action': action,
        'get_course': get_course,
        'attendance_report': attendance_report,
        'total_present': total_present,
        'total_class': total_class
    }
    return render(request,'Student/view_attendance.html',context)