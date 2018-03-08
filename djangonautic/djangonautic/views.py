from django.http import HttpResponse  ### send response to user when they request the page back.

### we need to two functions according to the urls we set up in the urls.py file.
### we dont need to set function for admin 


def homepage(request):
    return HttpResponse('homepage')

def about(request):  ### response to about url.  request object parameter. 
    return HttpResponse('about')
