from django.shortcuts import render,redirect
from app.models import Stuff, Stuff_Notification, Stuff_Leave, Stuff_Feedback, Course, Student, Department, Student_Result,Attendance, Attendance_Report
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import speech_recognition as sr
import pyttsx3

@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    stuff_count = Stuff.objects.all().count()
    department_count = Department.objects.all().count()
    course_count = Course.objects.all().count()
    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    context = {
        'student_count': student_count,
        'stuff_count': stuff_count,
        'department_count': department_count,
        'course_count': course_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
    return render(request,'Stuff/home.html',context)

@login_required(login_url='/')
def NOTIFICATIONS(request):
    stuff=Stuff.objects.filter(admin=request.user.id)
    for i in stuff:
        stuff_id=i.id
        notification=Stuff_Notification.objects.filter(stuff_id=stuff_id)
    context={
        'notification': notification,
    }
    return render(request,'Stuff/notifications.html',context)

@login_required(login_url='/')
def MARK_AS_DONE(request,status):
    notification=Stuff_Notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('notifications')


@login_required(login_url='/')
def STUFF_APPLY_LEAVE(request):
    stuff=Stuff.objects.filter(admin=request.user.id)
    for i in stuff:
        stuff_id=i.id
        stuff_leave_history=Stuff_Leave.objects.filter(stuff_id = stuff_id)
    context={
        'stuff_leave_history': stuff_leave_history,
    }
    return render(request,'Stuff/apply_leave.html',context)

@login_required(login_url='/')
def STUFF_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date=request.POST.get('leave_date')
        leave_message=request.POST.get('leave_message')
        leave_file = request.FILES.get('leave_file')
        stuff=Stuff.objects.get(admin = request.user.id)
        leave = Stuff_Leave(
            stuff_id=stuff,
            date = leave_date,
            message = leave_message,
            mfile= leave_file,
        )
        leave.save()
        messages.success(request,'Leave Successfully Sent')
    return redirect('stuff_apply_leave')


def STUFF_FEEDBACK(request):
    stuff_id=Stuff.objects.get(admin=request.user.id)
    feedback_history=Stuff_Feedback.objects.filter(stuff_id=stuff_id)
    context={
        'feedback_history': feedback_history,
    }
    return render(request,'Stuff/stuff_feedback.html',context)


def FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback=request.POST.get('feedback_message')
        stuff=Stuff.objects.get(admin=request.user.id)
        stuff_feedback=Stuff_Feedback(
            stuff_id=stuff,
            feedback=feedback,
            feedback_reply="",
        )
        stuff_feedback.save()
        messages.success(request,'Feedback Are Successfully Sent')
        return redirect('stuff_feedback')


def ADD_RESULT(request):
    staff=Stuff.objects.get(admin=request.user.id)
    course=Course.objects.filter(stuff_id=staff)
    # department=Department.objects.all()
    action=request.GET.get('action')
    get_course=None
    get_dept=None
    students=None
    if action is not None:
        if request.method=='POST':
            course_id=request.POST.get('course_id')
            # department_id=request.POST.get('department_id')
            get_course=Course.objects.get(id=course_id)
            # get_dept=Department.objects.get(id=department_id)
            course=Course.objects.filter(id=course_id)
            for i in course:
                semester=i.semester_id.id
                department_id=i.department_id.id
                # get_dept=i.department_id.dept_name
                get_dept = Department.objects.get(id=department_id)
                students=Student.objects.filter(semester_id=semester).filter(department_id=department_id).order_by('student_rid')

    context={
        'course': course,
        # 'department': department,
        'action': action,
        'get_course': get_course,
        'get_dept': get_dept,
        'students': students
    }
    return render(request,'Stuff/add_result.html',context)


def SAVE_RESULT(request):
    if request.method=='POST':
        course_id=request.POST.get('course_id')
        department_id=request.POST.get('department_id')
        student_id=request.POST.get('student_id')
        assignment_mark=request.POST.get('assignment_mark')
        exam_mark=request.POST.get('exam_mark')
        print(course_id)

        get_course=Course.objects.get(id=course_id)
        get_student=Student.objects.get(admin=student_id)
        get_department = Department.objects.get(id=department_id)

        check_exists=Student_Result.objects.filter(course_id=get_course,student_id=get_student).exists()
        if check_exists :
            result=Student_Result.objects.get(course_id=get_course,student_id=get_student)
            result.assignment_mark=assignment_mark
            result.exam_mark=exam_mark
            result.save()
            messages.success(request,'Result Are Successfully Updated ')
            return redirect('add_result')
        else:
            result=Student_Result(
                student_id=get_student,
                course_id=get_course,
                department_id=get_department,
                semester_id=get_course.semester_id,
                assignment_mark=assignment_mark,
                exam_mark=exam_mark,
            )
            result.save()
            messages.success(request, 'Result Are Successfully Added ')
            return redirect('add_result')
    return render(request,'')


def STUFF_TAKE_ATTENDANCE(request):
    staff = Stuff.objects.get(admin=request.user.id)
    course = Course.objects.filter(stuff_id=staff)
    action=request.GET.get('action')
    get_course=None
    students=None
    if action is not None:
        if request.method=='POST':
            course_id=request.POST.get('course_id')
            get_course=Course.objects.get(id=course_id)

            course=Course.objects.filter(id=course_id)
            for i in course:
                semester_id=i.semester_id.id
                students=Student.objects.filter(semester_id=semester_id).order_by('student_rid')

    context={
        'course': course,
        'get_course': get_course,
        'action': action,
        'students': students,
    }
    return render(request,'Stuff/take_attendance.html',context)


def STUFF_SAVE_ATTENDANCE(request):
    if request.method=='POST':
        course_id=request.POST.get('course_id')
        attendance_date=request.POST.get('attendance_date')
        student_id=request.POST.getlist('student_id')

        course=Course.objects.get(id=course_id)
        attendance = Attendance(
            course_id=course,
            attendance_date=attendance_date,
            semester=course.semester_id,
        )
        attendance.save()

        for i in student_id:
            student_id=i
            p_student= Student.objects.get(id=student_id)
            attendance_report= Attendance_Report(
                student_id=p_student,
                attendance_id=attendance,
            )
            attendance_report.save()
        messages.success(request,'Attendance Are Successfully Added')
        return redirect('staff_take_attendance')


def STUFF_VIEW_ATTENDANCE(request):
    staff = Stuff.objects.get(admin=request.user.id)
    course = Course.objects.filter(stuff_id=staff)
    action = request.GET.get('action')
    get_course=None
    attendance_date=None
    attendance_report=None
    if action is not None:
        if request.method=='POST':
            course_id=request.POST.get('course_id')
            attendance_date=request.POST.get('attendance_date')
            get_course=Course.objects.get(id=course_id)

            attendance=Attendance.objects.filter(course_id=get_course, attendance_date=attendance_date)
            for i in attendance:
                attendance_id=i.id
                attendance_report=Attendance_Report.objects.filter(attendance_id=attendance_id)

    context={
        'course': course,
        'action': action,
        'get_course': get_course,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }
    return render(request,'Stuff/view_attendance.html',context)


def STUFF_VIEW_RESULT(request):
    staff = Stuff.objects.get(admin=request.user.id)
    course = Course.objects.filter(stuff_id=staff)
    action = request.GET.get('action')
    get_course = None
    student_result=None
    if action is not None:
        if request.method=='POST':
            course_id=request.POST.get('course_id')
            get_course=Course.objects.get(id=course_id)
            student_result=Student_Result.objects.filter(course_id=get_course)

    context={
        'course': course,
        'action': action,
        'get_course': get_course,
        'student_result': student_result,
    }
    return render(request,'Stuff/view_result.html',context)




voice = sr.Recognizer()
def SPEAK(request):
    text=None
    if request.method=='POST':
        print('speak:')
        with sr.Microphone() as source:
            audio = voice.listen(source)
            try:
                text = voice.recognize_google(audio)
                print(text)

            except:
                print('your voice is not clear')

    context={
        'text': text,
    }
    return render(request,'Stuff/voice.html',context)