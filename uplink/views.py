from django.shortcuts import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse("test")