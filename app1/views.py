from django.shortcuts import render

# Create your views here.
def jinja1(request):
    d={'name':'chalapathirao'}
    return render(request,'h1.html',d)