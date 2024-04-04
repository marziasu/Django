from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method=='POST':
        user=EmailBackEnd.authenticate(request,
                                       username=request.POST.get('email'),
                                       password=request.POST.get('password'))
        if(user!=None):
            login(request,user)
            user_type=user.user_type
            if user_type=='1':
                return redirect('hod_home')
            elif user_type=='2':
                return redirect('stuff_home')
            elif user_type=='3':
                return redirect('student_home')
            else:
                messages.error(request,'Email and Password are invalid')
                return redirect('login')
        else:
            messages.error(request, 'Email and Password are invalid')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user=CustomUser.objects.get(id=request.user.id)
    context={
        'user':user
    }
    return render(request, 'profile.html',context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method=='POST':
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')
        try:
            customUser=CustomUser.objects.get(id=request.user.id)
            customUser.first_name=first_name
            customUser.last_name=last_name

            if password!=None and password!="":
                customUser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customUser.profile_pic=profile_pic
            customUser.save()
            messages.success(request,'Your Profile Update Successfully!')
            return redirect('profile')
        except:
            messages.error(request,'Failed To Update Your Profile!')

    return render(request,'profile.html')