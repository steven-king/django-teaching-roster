# Create your views here.
from django.shortcuts import render

def home(request):
    context = {'message': 'This is a dynamic message variable!'}
    return render(request, "base.html", context)
    