from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Home!')
    #Changed from index to theme
    return render(request, 'home/theme.html')
