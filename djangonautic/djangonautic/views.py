from django.http import HttpResponse
from django.shortcuts import render ### render the page, so we need to import render 

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html') ### render( request, page)

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
