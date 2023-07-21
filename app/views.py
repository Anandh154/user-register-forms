from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFOD=UserForm(request.POST)
        PFOD=ProfileForm(request.POST,request.FILES)
        if UFOD.is_valid() and PFOD.is_valid():
            NSUFOD=UFOD.save(commit=False)
            submittedpw=UFOD.cleaned_data['password']
            NSUFOD.set_password(submittedpw)
            NSUFOD.save()
            NSPOD=PFOD.save(commit=False)
            NSPOD.username=NSUFOD
            NSPOD.save()

            send_mail('Registritation','registration is successfully done','lovelyanandhkarnam244@gmail.com',[NSUFOD.email],fail_silently=False)
            return HttpResponse('registration is successfully done')
    return render(request,'registration.html',d)

def home(request):
    if  request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def user_login(request):
    if  request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('not active user')
        else:
            return HttpResponse('invalid details')
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))