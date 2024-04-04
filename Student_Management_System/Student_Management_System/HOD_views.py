from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Session, Department , CustomUser, Student, Stuff, Course, Stuff_Notification, Stuff_Leave, Stuff_Feedback, Student_Notification,Semester
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    student_count=Student.objects.all().count()
    stuff_count=Stuff.objects.all().count()
    department_count=Department.objects.all().count()
    course_count=Course.objects.all().count()
    student_gender_male=Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    context={
        'student_count': student_count,
        'stuff_count': stuff_count,
        'department_count': department_count,
        'course_count': course_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
    return render(request,'HOD/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
        department=Department.objects.all()
        semester = Semester.objects.all()
        session=Session.objects.all()

        if request.method=='POST':
            profile_pic=request.FILES.get('profile_pic')
            student_rid = request.POST.get('student_rid')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            gender = request.POST.get('gender')
            department_id = request.POST.get('department_id')
            session_id = request.POST.get('session_id')
            semester_id = request.POST.get('semester_id')
            address = request.POST.get('address')

            if Student.objects.filter(student_rid=student_rid).exists():
                messages.warning(request,' This ID is already taken.')
                return redirect('add_student')
            if CustomUser.objects.filter(email=email).exists():
                messages.warning(request,'Email is already taken.')
                return redirect('add_student')
            if CustomUser.objects.filter(username=user_name).exists():
                messages.warning(request,'User Name is already taken.')
                return redirect('add_student')
            else:
                user=CustomUser(
                    profile_pic=profile_pic,
                    first_name=first_name,
                    last_name=last_name,
                    username=user_name,
                    email=email,
                    user_type=3

                )
                user.set_password(password)
                user.save()

                department=Department.objects.get(id=department_id)
                session=Session.objects.get(id=session_id)
                semester = Semester.objects.get(id=semester_id)

                student=Student(
                    admin=user,
                    student_rid=student_rid,
                    gender=gender,
                    department_id=department,
                    session_id=session,
                    semester_id=semester,
                    address=address,
                )
                student.save()
                messages.success(request, user.first_name+" "+user.last_name+" Are Successfully Added !")
                return redirect('add_student')
        context={
            'department': department,
            'semester': semester,
            'session': session
        }
        return render(request,'HOD/add_student.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student=Student.objects.all().order_by('student_rid')
    context={
        'student':student,
    }
    return render(request,'HOD/view_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student=Student.objects.filter(id=id)
    department=Department.objects.all()
    semester = Semester.objects.all()
    session=Session.objects.all()
    context={
        'student': student,
        'department': department,
        'session': session,
        'semester': semester,
    }
    return render(request,'HOD/edit_student.html',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == 'POST':
        student_id=request.POST.get('student_id')
        student_rid = request.POST.get('student_rid')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        department_id = request.POST.get('department_id')
        session_id = request.POST.get('session_id')
        semester_id = request.POST.get('semester_id')
        address = request.POST.get('address')

    user=CustomUser.objects.get(id=student_id)

    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.user_name=user_name
    if password != None and password !=" ":
        user.set_password(password)

    if profile_pic != None and profile_pic !=" ":
        user.profile_pic=profile_pic
    user.save()

    student=Student.objects.get(admin=student_id)
    student.address=address
    student.gender=gender
    student.student_rid=student_rid

    department=Department.objects.get(id=department_id)
    student.department_id = department

    session=Session.objects.get(id=session_id)
    student.session_id=session

    semester = Semester.objects.get(id=semester_id)
    student.semester_id = semester

    student.save()
    messages.success(request,'Record Are Successfully Updated!')
    return redirect('view_student')

    return render(request,'HOD/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student=CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted!')

    return redirect('view_student')

@login_required(login_url='/')
def ADD_DEPARTMENT(request):

    if request.method=='POST':
        department_name=request.POST.get('department_name')
        hod_name = request.POST.get('hod_name')
        department=Department(
            dept_name=department_name,
            hod_name=hod_name,
        )
        department.save()
        messages.success(request,'Record Are Successfully Added')
        return redirect('add_department')
    return render(request,'HOD/add_department.html')

@login_required(login_url='/')
def VIEW_DEPARTMENT(request):
    department=Department.objects.all()
    context={
        'department': department,
    }

    return render(request,'HOD/view_department.html',context)

@login_required(login_url='/')
def EDIT_DEPARTMENT(request,id):
    department=Department.objects.filter(id=id)
    context={
        'department':department,
    }
    return render(request,'HOD/edit_department.html',context)

@login_required(login_url='/')
def UPDATE_DEPARTMENT(request):
    if request.method=="POST":
        department_id=request.POST.get('department_id')
        department_name=request.POST.get('department_name')
        hod_name=request.POST.get('hod_name')

        department = Department.objects.get(id=department_id)
        department.dept_name=department_name
        department.hod_name=hod_name
        department.save()
        messages.success(request,'Department is Successfully Updated!')
        return redirect('view_department')

    return render(request, 'HOD/edit_department.html')

@login_required(login_url='/')
def DELETE_DEPARTMENT(request,id):
    department=Department.objects.get(id=id)
    department.delete()
    messages.success(request,'Department Are Successfully Deleted!')
    return redirect('view_department')

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method=='POST':
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')
        session=Session(
            session_start=session_start,
            session_end=session_end
        )
        session.save()
        messages.success(request,'Session Details Are Successfully Added!')
        redirect('add_session')
    return render(request,'HOD/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session=Session.objects.all()
    context={
        'session':session,
    }
    return render(request,'HOD/view_session.html',context)

@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session = Session.objects.filter(id=id)
    context = {
        'session': session,
    }
    return render(request, 'HOD/edit_session.html', context)

@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method=="POST":
        session_id=request.POST.get('session_id')
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')

        session = Session.objects.get(id=session_id)
        session.session_start=session_start
        session.session_end=session_end
        session.save()
        messages.success(request,'Session is Successfully Updated!')
        return redirect('view_session')

    return render(request, 'HOD/edit_session.html')

@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session=Session.objects.filter(id=id)
    session.delete()
    messages.success(request,'Session Are Successfully Deleted!')
    return redirect('view_session')

@login_required(login_url='/')
def ADD_STUFF(request):
    if request.method=="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address=request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already taken.')
            return redirect('add_student')
        if CustomUser.objects.filter(username=user_name).exists():
            messages.warning(request,'User Name is already taken.')
            return redirect('add_stuff')
        else:
            user=CustomUser(
                profile_pic=profile_pic,
                first_name=first_name,
                last_name=last_name,
                username=user_name,
                email=email,
                user_type=2

            )
            user.set_password(password)
            user.save()

            stuff= Stuff(
                admin=user,
                gender=gender,
                address=address,
            )
            stuff.save()
            messages.success(request, user.first_name+" "+user.last_name+" Are Successfully Added !")
            return redirect('add_stuff')
    return render(request,'HOD/add_stuff.html')

@login_required(login_url='/')
def VIEW_STUFF(request):
    stuff = Stuff.objects.all()
    context = {
        'stuff': stuff,
    }
    return render(request, 'HOD/view_stuff.html', context)

@login_required(login_url='/')
def EDIT_STUFF(request,id):
    stuff = Stuff.objects.filter(id=id)
    context = {
        'stuff': stuff,
    }
    return render(request, 'HOD/edit_stuff.html', context)

@login_required(login_url='/')
def UPDATE_STUFF(request):
    if request.method == 'POST':
        stuff_id=request.POST.get('stuff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

    user=CustomUser.objects.get(id=stuff_id)
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.user_name=user_name

    if password != None and password !=" ":
        user.set_password(password)
    if profile_pic != None and profile_pic !=" ":
        user.profile_pic=profile_pic
    user.save()

    stuff=Stuff.objects.get(admin=stuff_id)
    stuff.address=address
    stuff.gender=gender
    print(stuff.gender)
    stuff.save()
    messages.success(request,'Stuff Are Successfully Updated!')
    return redirect('view_stuff')

    return render(request,'HOD/edit_stuff.html')

@login_required(login_url='/')
def DELETE_STUFF(request,admin):
    stuff= CustomUser.objects.get(id=admin)
    stuff.delete()
    messages.success(request, 'Stuff Are Successfully Deleted!')
    return redirect('view_stuff')

@login_required(login_url='/')
def ADD_COURSE(request):
    department=Department.objects.all()
    semester = Semester.objects.all()
    stuff=Stuff.objects.all()
    if request.method=='POST':
        course_name=request.POST.get('course_name')
        department_id=request.POST.get('department_id')
        department = Department.objects.get(id=department_id)
        semester_id = request.POST.get('semester_id')
        semester = Semester.objects.get(id=semester_id)
        stuff_id=request.POST.get('stuff_id')
        stuff = Stuff.objects.get(id=stuff_id)
        if Course.objects.filter(name=course_name).exists():
            messages.warning(request, 'Course Name is already taken.')
            return redirect('add_course')

        course=Course(
            name=course_name,
            department_id=department,
            semester_id=semester,
            stuff_id=stuff,
        )
        course.save()
        messages.success(request,'Course Are Successfully Added')
        return redirect('add_course')
    context={
        'department': department,
        'semester': semester,
        'stuff': stuff,
    }
    return render(request,'HOD/add_course.html',context)

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request,'HOD/view_course.html',context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.filter(id=id)
    department=Department.objects.all()
    semester = Semester.objects.all()
    stuff=Stuff.objects.all()
    context = {
        'course': course,
        'department': department,
        'semester': semester,
        'stuff': stuff,
    }
    return render(request, 'HOD/edit_course.html', context)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')
        department_id=request.POST.get('department_id')
        semester_id = request.POST.get('semester_id')
        stuff_id = request.POST.get('stuff_id')
        department = Department.objects.get(id=department_id)
        semester = Semester.objects.get(id=semester_id)
        stuff = Stuff.objects.get(id=stuff_id)
        course=Course(
            id=course_id,
            name=course_name,
            department_id=department,
            semester_id=semester,
            stuff_id=stuff
        )

        course.save()
        messages.success(request, 'Course is Successfully Updated!')
        return redirect('view_course')

    return render(request, 'HOD/edit_course.html')

@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course=Course.objects.filter(id=id)
    course.delete()
    messages.success(request,'Course Are Successfully Deleted!')
    return redirect('view_course')

@login_required(login_url='/')
def STUFF_SEND_NOTIFICATION(request):
    stuff=Stuff.objects.all()
    see_notification=Stuff_Notification.objects.all().order_by('-id')[0:5]
    context={
        'stuff': stuff,
        'see_notification': see_notification,
    }
    return render(request,'HOD/stuff_send_notification.html',context)

@login_required(login_url='/')
def SAVE_STUFF_NOTIFICATION(request):
    if request.method == 'POST':
        stuff_id=request.POST.get('stuff_id')
        message=request.POST.get('message')
        stuff=Stuff.objects.get(admin=stuff_id)
        notification=Stuff_Notification(
            stuff_id=stuff,
            message=message,
        )
        notification.save()
        messages.success(request,'Notification Are Successfully Send!')
    return redirect('stuff_send_notification')

@login_required(login_url='/')
def STUFF_LEAVE_VIEW(request):
    stuff_leave=Stuff_Leave.objects.all()
    context={
        'stuff_leave': stuff_leave,
    }
    return render(request,'HOD/stuff_leave_view.html',context)

@login_required(login_url='/')
def APPROVE_LEAVE(request,id):
    leave=Stuff_Leave.objects.get(id=id)
    leave.status=1
    leave.save()
    return redirect('stuff_leave_view')

@login_required(login_url='/')
def DISAPPROVE_LEAVE(request,id):
    leave = Stuff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('stuff_leave_view')

@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff_feedback=Stuff_Feedback.objects.all()
    context={
        'staff_feedback': staff_feedback,
    }
    return render(request,'HOD/staff_feedback.html',context)

@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback_id=request.POST.get('feedback_id')
        feedback_reply=request.POST.get('feedback')
        feedback=Stuff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_reply
        feedback.save()
        messages.success(request,'reply successfully')
    return redirect('staff_feedback')

@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATION(request):
    student= Student.objects.all()
    notification=Student_Notification.objects.all()
    context={
        'student': student,
       'notification': notification,
    }
    return render(request,'HOD/student_notification.html',context)

@login_required(login_url='/')
def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == 'POST':
        student_id=request.POST.get('student_id'),
        message=request.POST.get('message')
        student=Student.objects.get(admin=student_id)
        notification=Student_Notification(
            student_id=student,
            message=message,
        )
        notification.save()
        messages.success(request,'Notification Are Successfully Send!')
    return redirect('student_send_notification')


def LEAVE_MESSAGE_VIEW(request,id):
    stuff_leave=Stuff_Leave.objects.filter(id=id)
    for i in stuff_leave:
        print(i.mfile)
    context={
        'stuff_leave': stuff_leave,
    }
    return render(request,'HOD/leave_message_view.html',context)