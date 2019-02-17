from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login/")
def Main(request):
    return render(request, 'questionableansible/main.html')

@login_required(login_url="/accounts/login/")
def Create(request):
    if request.method == "POST":
        form = forms.GCEInstance(request.POST)
        if form.is_valid():
            # This is where it will serialize the information and send
            # to answerableansible
            return redirect('questionableansible:main')
    else:
        form = forms.GCEInstance()
    return render(request, 'questionableansible/create.html', {'form': form})


@login_required(login_url="/accounts/login/")
def Credentials(request):
    if request.method == "POST":
        form = forms.GCPInfo(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.User = request.user 
            instance.save()
            return redirect('questionableansible:main')
    else:
        form = forms.GCPInfo()
    return render(request, 'questionableansible/credentials.html', {'form': form})