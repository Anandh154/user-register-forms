from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

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
            return HttpResponse('registration is successfully done')
    return render(request,'registration.html',d)