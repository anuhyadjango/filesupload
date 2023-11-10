from django.shortcuts import render
from .forms import *

# Create your views here.
#def home(request):
    #return render(request,'resumes/home.html')

def home(request):
    form = resumeform()
    if request.method == "POST":
        form = resumeform(request.POST,request.FILES)
        if form.is_valid():
            #n1 = form.cleaned_data.get('fname')
            form.save()
            obj = form.instance
            return render(request,"resumes/home.html",{'form':form,'obj':obj})
        else:
            return render(request,'resumes/home.html',{'form':form})
    else:
        msg = "plz all the fields"
        return render(request,'resumes/home.html',{'form':form,'msg':msg})

def viewprofiles(request):
    if request.method == 'GET':
        resumes=profiles.objects.all()
        return render(request,'resumes/details.html',{'resumes':resumes})
