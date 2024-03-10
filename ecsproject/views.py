from django.shortcuts import render
from django.core.mail import mail_admins
from django.http import HttpResponse


def homepage(request):
    return render(request,"home.html")

def about(request):
    return render(request, "about.html")


def aboutprojectfunction(request):
    return render(request, "project.html")

def contactusfunction(request):
    return render(request, "contactus.html")

#def democontactfunction(request):

    #return render(request, "democontact.html")



def democontactfunction(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        sender = request.POST.get('sender', '')
        if subject and message and sender:
            mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
            return HttpResponse('Success')
    return HttpResponse('Error')
