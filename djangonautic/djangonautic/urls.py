from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls), ### after regular express, it comes with a function
    url(r'^about/$', views.about), ### $ sign means nothing comes after, it ends with about
    url(r'^$', views.homepage), ### home page usually has nothing after.  for instance: .com/
]

### after we create the view url, we create a new view file.  views.py . inside the views files, is where we create function that will fire 
### when users visit certain url
