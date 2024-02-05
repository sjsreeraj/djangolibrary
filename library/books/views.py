from django.db.models import Q
from books.forms import bookform
from django.shortcuts import render
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        d=request.FILES['d']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=d,cover=i)
        b.save()
        return viewbooks(request)


    return render(request,'addbooks.html')


@login_required

def viewbooks(request):
    k=Book.objects.all()
    return render(request,'viewbooks.html',{'b':k})
@login_required

def add1(request):
    if(request.method=="POST"):#after submission
        form=bookform(request.POST)#create form object initialize wuth values inside request.POST
        if form.is_valid():
            form.save()#saves form object in db  model book
            return viewbooks(request)

    form=bookform()
    return render(request,'addbooks1.html',{'form':form})

@login_required

def fact(request):
    if(request.method=="POST"):
        num=int(request.POST['n'])
        f=1
        for i in range(1,num+1):
            f=f*i
        return render(request,'FACT.HTML',{'fact':f})

    return render(request,'FACT.html')

@login_required

def detail(request,p):
    b=Book.objects.get(id=p)
    return render(request,'bookdetail.html',{'b':b})
@login_required

def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return viewbooks(request)
@login_required

def edit(request,p):
    b=Book.objects.get(id=p)

    if(request.method=="POST"):#after submission
        form=bookform(request.POST,request.FILES,instance=b)#create form object initialize wuth values inside request.POST
        if form.is_valid():
            form.save()#saves form object in db  model book
            return viewbooks(request)


    form=bookform(instance=b)
    return render(request,'edit.html',{'form':form})

def search(request):
    b= None
    q= ""
    if (request.method=="POST"):
        q=request.POST['q']
        b=Book.objects.filter(Q(title__icontains=q)| Q(author__icontains=q))
    return render(request,'search.html',{'q':q,'b':b})

