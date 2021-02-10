from django.shortcuts import render


def index(request):
    return render(request, 'pyecolib/home/index.html')

def installation(request):
    return render(request, 'pyecolib/installation/installation.html')
