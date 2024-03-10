from django.db.models import Q
from django.shortcuts import render,HttpResponse,redirect
from .forms import JobsForm,JobprofileForm 
from .models import Aspirant,Employer,Jobprofile,Job,Applyjob


# Create your views here.
def aspiranthomefunction(request):
    aspuname = request.session["aspuname"]
    joblist = Job.objects.all()
    return render(request,"asphome.html",{"aspuname" : aspuname,"joblist":joblist})

def emphomefunction(request):
    empuname = request.session["empuname"]
    asplist = Aspirant.objects.all()
    return render(request,"emphome.html",{"empuname" : empuname,"asplist":asplist})

def aspprofilefunction(request):
    aspuname = request.session["aspuname"]
    updateprofile = JobprofileForm()
    updatejobdata = JobprofileForm(request.POST)
    if updatejobdata.is_valid():
        updatejobdata1 = updatejobdata.save(commit = False)
        updatejobdata1.aspuname = aspuname
        updatejobdata1.save()
        msg = "Profile Updated Successfully"
        return render(request, "aspprofile.html",{"updateprofile" : updateprofile,"msg":msg})
    else:
        msg = "Failed to update profile"
        return render(request, "aspprofile.html",{"updateprofile" : updateprofile,"msg":msg})
    return render(request, "aspprofile.html")
        

def empprofilefunction(request):
    return render(request, "empprofile.html")

def registrationfunction(request):
    if request.method == "POST":
        fullname=request.POST['fullname']
        dob=request.POST['dob']
        email = request.POST['email']
        uname = request.POST['uname']
        pwd =request.POST['pwd']
        cpwd = request.POST['cpwd']
        dept = request.POST['dept']
        phno = request.POST['phno']
        
        flag1 = Aspirant.objects.filter(email=email)
        flag2 = Employer.objects.filter(email=email)
        print(flag1)
        print(flag2)

        if(pwd != cpwd):
            msg="PASSWORDS DOES NOT MATCH"
            return render(request,"registration.html",{"msg" : msg})
        
            """if flag1 is not None or flag2 is not None:
                msg="Email already exists"
                return render(request,"registration.html",{"msg" : msg})"""
        elif(dept == 'Employer'):
            new_emp = Employer(fullname = fullname,dob=dob,email=email,empuname=uname,pwd=pwd,cpwd=cpwd,dept=dept,phno=phno)
            print(new_emp)
            new_emp.save()
            msg="registration success as employer"
            return render(request,"login.html",{"msg" : msg})
        else:
            new_asp = Aspirant(fullname = fullname,dob=dob,email=email,aspuname=uname,pwd=pwd,cpwd=cpwd,dept=dept,phno=phno)
            print(new_asp)
            new_asp.save()
            msg="registration success as aspirant"
            return render(request,"login.html",{"msg" : msg})
    return render(request, "registration.html")


def loginfunction(request):
    return render(request, "login.html")


def checkuserlogin(request):
    uname=request.POST["uname"]
    pwd=request.POST["pwd"]

    aspflag=Aspirant.objects.filter( Q(aspuname=uname) & Q(pwd=pwd) )
    empflag=Employer.objects.filter( Q(empuname=uname) & Q(pwd=pwd) )

    if aspflag:
        user=Aspirant.objects.get(aspuname=uname)
        request.session["aspuname"]=user.aspuname
        joblist = Job.objects.all()
        return render(request,"asphome.html",{"aspuname":user.aspuname,"joblist":joblist})
    if empflag:
        user=Employer.objects.get(empuname=uname)
        request.session["empuname"]=user.empuname
        asplist = Aspirant.objects.all()
        return render(request,"emphome.html",{"empuname":user.empuname,"asplist":asplist})
    else:
        msg="Login Failed"
        return render(request,"login.html",{"msg" : msg})


def asplogout(request):
    try:
        print(request.session['aspuname'])
        del request.session['aspuname']
        print(request.session['aspuname'])
    except:
        return redirect('/')
    return redirect('/')


def emplogout(request):
    try:
        print(request.session['empuname'])
        del request.session['empuname']
        print(request.session['empuname'])
    except:
        return redirect('/')
    return redirect('/')


def aboutaspirant(request,aspuname):
    return render(request, "aboutaspirants.html",{"aspuname" : aspuname})


def addjob(request):
    empuname = request.session["empuname"]
    print(empuname)
    job = JobsForm()
    jobdata = JobsForm(request.POST)
    if jobdata.is_valid():
        jobdata1 = jobdata.save(commit = False)
        jobdata1.empuname = empuname
        jobdata1.save()
        msg = "Job added Successfully"
        return render(request, "addjob.html",{"jform" : job,"msg":msg})
    else:
        msg = "Failed to add Job    "
        return render(request, "addjob.html",{"jform" : job,"msg":msg})
    return render(request, "addjob.html")


def applied (request,jid):
    aspuname = request.session["aspuname"]
    application = Applyjob(aspuname = aspuname,jid = jid)
    application.save()
    joblist = Job.objects.all()
    return render(request,"asphome.html",{"aspuname" : aspuname,"joblist":joblist})



def viewjobs(request):
    empuname = request.session["empuname"]
    joblist = Job.objects.filter(empuname = empuname).all()
    return render(request,"viewjobs.html",{"joblist":joblist})


def viewapplicants(request,jid):
    applicantlist = Applyjob.objects.filter(jid=jid).all()
    return render(request, "viewapplicants.html",{"applicantlist" : applicantlist}) 