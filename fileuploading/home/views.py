from django.shortcuts import render
from notifications import VerifyEmailNotification
from some_project.services import Service

# Create your views here.
def home(request):
    return render(request, 'home.html')

def other(request):
    context = {
    'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html', context)
