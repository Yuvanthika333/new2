from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Students,Stud

# Create your views here.
def index(request):
    return render(request,"index.html")

def aboutus(request):
    return render(request,"aboutus.html")
def adview(request):
    stud=Stud.objects.all()
    return render(request,"adview.html",{'stud':stud})

def edit(request,id):
    stud=Stud.objects.get(id=id)

    return render(request,"edit.html",{'stud':stud})
def search(request,id):
    stud=Stud.objects.get(id=id)
    stud=Stud.objects.all()

    return render(request,"edit.html",{'stud':stud})
def editrecord(request,id):
        stud_name=request.POST['stud_name']
        father_name=request.POST['father_name']
        email=request.POST['email']
        student_c=request.POST['student_c']
        course=request.POST['course']
        stud=Stud.objects.get(id=id)
        stud.stud_name=stud_name
        stud.father_name=father_name
        stud.email=email
        stud.student_c=student_c
        stud.course=course
        stud.save()
        return render(request,"adview.html")

def delete(request,id):
    stud=Stud.objects.get(id=id)
    stud.delete()

    return redirect("/adview") 


def contactus(request):
    return render(request,"contactus.html")

def studentlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Students.objects.filter(username=username).exists():
            messages.info(request,"successfull")
            return redirect("/stud_dash")
        elif Students.objects.filter(password=password).exists():
            messages.info(request,"successfull")
            return redirect("/studentlogin")  
        else:
            messages.info(request,"Please Registor first")
    return render(request,"studentlogin.html")

def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpass=request.POST.get('cpass')
        if Students.objects.filter(username=username).exists():
            messages.info(request,"successfull")
            return redirect("/admin_reg")
        elif Students.objects.filter(password=password).exists():
            messages.info(request,"successfull")
            return redirect("/adminlogin")
        elif Students.objects.filter(cpass=cpass).exists():
            messages.info(request,"successfull")
            return redirect("/adminlogin")
          
        else:
            messages.info(request,"Please Registor first")
           
    return render(request,"adminlogin.html")

def registor(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpass']
        new=Students.objects.create(username=username,password=password,cpass=cpass)
        new.save()
        return redirect("/")
        
    return render(request,"registor.html")
    

def admin_reg(request):
    studs=Stud.objects.all()
   
   
    if request.method=='POST':

        stud_name1=request.POST['stud_name']
        father_name=request.POST['father_name']
        email=request.POST['email']
        password=request.POST['password']
        con_password=request.POST['con_password']
        student_c=request.POST['student_c']
        course=request.POST['course']
        stud=Stud.objects.create(stud_name=stud_name1,father_name=father_name,email=email,password=password,con_password=con_password,student_c=student_c,course=course)
        stud.save()
        stud.objects.all()
      
        return render (request,'admin_reg.html',{'stud': stud,'studs':studs})
    return render(request,"admin_reg.html")

def stud_dash(request):
        stud = Students.objects.all()
        context = {
            'studs': stud

        }
        print(context)
        return render(request,"stud_dash.html",context)
