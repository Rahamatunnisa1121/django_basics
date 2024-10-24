from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#view is a request handler
#also called action
#takes a req and returns a res

def say_hello(request):
    return render(request,'hello.html',{'name':'Ruhi'})
    #returns response object
    #When the template is rendered, Django replaces {{ name }} in the template with the value Ruhi.