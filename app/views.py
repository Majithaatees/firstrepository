import smtplib
from django.contrib import messages
from django.shortcuts import render, redirect
from app.models import mydata, customers
from django.conf import settings
# Create your views here.
def index(request):
    if 'uname' in request.session:
        detail=mydata.objects.all()
        return render(request,"index.html",{"det":detail})
    else:
        return render(request,"register.html")
    return render(request,"login.html")
def show(request,id):
    deta=mydata.objects.get(id=id)
    return render(request,"show.html",{"det":deta})
def register(request):
    if request.method=="POST":
        name=request.POST['name']
        uname=request.POST['uname']
        passw=request.POST['password']
        cpass=request.POST['cpass']
        customers(name=name,uname=uname,password=passw,cpassword=cpass).save()
        return redirect('login')
    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        passw=request.POST['password']
        data=customers.objects.filter(uname=uname,password=passw)
        if data:
            request.session['uname']=uname
            return redirect('index')
        else:
            messages.error(request,"Enter valid username and password")
    return render(request,"login.html")
def logout(request):
    del request.session['uname']
    return render(request,"register.html")
def send_mail(request):
    if request.method=="POST":
        subject=request.POST["subject"]
        email_from=settings.EMAIL_HOST_USER
        passw=settings.EMAIL_HOST_PASSWORD
        recipient_list=request.POST["to"]
        message=request.POST["message"]
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(email_from,passw)
        header='To:'+recipient_list+'\n'+'From:'+email_from+'\n'+'subject:'+subject+'\n'
        content=header+message
        server.sendmail(email_from,recipient_list,content)
        server.quit()
        return redirect('index')
    return render(request,"sendmail.html")



