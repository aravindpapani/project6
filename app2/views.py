from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1> You are in index of APP2</h1>")

def sample1(request):
    return render(request,'app2/sample2.html')

def sample2(request):
    return render(request,'app2.html')