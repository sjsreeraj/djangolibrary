from django.shortcuts import render,redirect
from students.models import student
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from students.models import CustomUser
from django.http import HttpResponse
# Create your views here.
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        pl=request.POST['pl']
        n=request.POST['n']
        if(p==cp):
           user=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,place=pl,phone=n)
           user.save()
           return redirect('books:home')
        else:
          return HttpResponse("not same")


    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid")

    return render(request,'login.html')


@login_required

def user_logout(request):
    logout(request)
    return redirect('students:login')

def viewstudents(request):
    g=student.objects.all()

    return render(request,'viewstudents.html',{'s':g})
