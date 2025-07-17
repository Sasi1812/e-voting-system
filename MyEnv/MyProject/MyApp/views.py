from django.shortcuts import render
from . import models
url=''
def insert_initial():
    if not models.B.objects.exists():
        models.B.objects.create(vote="x",count=0)
        models.B.objects.create(vote="y",count=0)
        models.B.objects.create(vote="z",count=0)
def view1(request):
    insert_initial()
    if 'register' in request.POST:
        return render(request,'register.html')
    elif 'login' in request.POST:
        return render(request,'login.html')
    elif 'count' in request.POST:
        return render(request,'count.html')
    return render(request,'home.html')
def view2(request):
    if 'register' in request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        a=models.A.objects.filter(name=name)
        if len(a)==0:
            p=models.A(name=name,email=email,password=password)
            p.save()
            return render(request,'success.html',{'success':'successfully registered'})
        else:
            return render(request,'success.html',{'success':'Already registered'})
    return render(request,'register.html')
def view3(request):
    if 'back' in request.POST:
        return render(request,'home.html')
    return render(request,'success.html',{'success':" "})
def view4(request):
    if 'login' in request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')
        a=models.A.objects.filter(email=email).first()
        if a.password==password:
            return render(request,'vote.html',{'success':'successfully logged in'})
        else:
            return render(request,'login.html',{'success':'invalid credentials'})
    return render(request,'login.html',{'success':' '})
def view5(request):
    global url
    if 'vote' in request.POST:
        name=request.POST.get('name')
        a=models.A.objects.filter(name=name).first()
        if a.vote=='null':
            url=name
            print(url)
            return render(request,'vote1.html')
        else:
            return render(request,'vote.html',{'success':'Already voted'})
    elif 'back' in request.POST:
        return render(request,'home.html')
    return render(request,'vote.html',{'success':' '})
def view6(request):
    global url
    if 'click' in request.POST:
        a=request.POST.get('vote')
        b=models.B.objects.filter(vote=a).first()
        c=b.count
        c=c+1
        print('in vote1 url is',url)
        models.B.objects.filter(vote=a).update(count=c)
        models.A.objects.filter(name=url).update(vote=a)
        na=models.A.objects.filter(name=url).first()
        return render(request,'vote1.html',{"success":'voted successfully'})
    elif 'back' in request.POST:
        return render(request,'home.html')
    return render(request,'vote1.html',{'success':' '})
def view7(request):
    if 'click' in request.POST:
       a=models.B.objects.all()
       return render(request,'count.html',{'a':a})
    elif 'back' in request.POST:
        return render(request,'home.html')
    return render(request,'count.html',{'a':' '})
   
def view8(request):
    if 'submit' in request.POST:
        b=request.POST.get("email")
        a=request.POST.get("password")
        models.A.objects.filter(email=b).update(password=a)
        return render(request,'forgot.html',{'a':'changed successfully'})
    elif 'back' in request.POST:
        return render(request,'home.html')
    return render(request,'forgot.html',{'a':' '})



# Create your views here.
