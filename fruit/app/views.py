from django.shortcuts import render
from.models import students

def home(r):
    return render(r,'home.html')

def add(r):
   return render(r,'add.html')

def data(r):
    a = r.POST['n1']
    b = r.POST['n2']
    c = r.POST['n3']
    d = r.POST['n4']
    e = r.FILES['n5']
    d = students(roll=a, name=b, age=c, mark=d, image=e)
    d.save()
    return render(r, 'add.html')

def all(r):
    data = students.objects.all()
    return render(r,'alldisplay.html',{'d':data})

def show(r):
    data = students.objects.all()

    return render(r,'display.html',{'d':data})

def show2(r):
    return render(r,'display.html')

def srchome(r):
    return render(r,'search.html')

def search(r):
    a = r.POST['n1']
    data= students.objects.filter(roll=a)
    return render(r,'sr_display.html',{'d':data})

def update(r):
    b = r.POST['r']
    n = r.POST['n']
    a = r.POST['ag']
    m = r.POST['m']
    i = r.FILES['jpg']
    students.objects.filter(roll=b).update(name=n, age=a,mark=m, image=i)
    data = students.objects.all()
    return render(r, 'updated.html',{'d1':data})

def delete(r):
    b = r.POST['r']
    data=students.objects.filter(roll=b)
    data.delete()
    return render(r,'updated.html',{'d':data})