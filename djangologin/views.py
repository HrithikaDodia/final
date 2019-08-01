from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request,'index.html',{'user':request.user})

def base(request):
    return HttpResponse('<h1>Base</h1>')