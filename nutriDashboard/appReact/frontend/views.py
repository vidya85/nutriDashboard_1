from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    print("inside view")
    return render(request, 'frontend/index.html')
