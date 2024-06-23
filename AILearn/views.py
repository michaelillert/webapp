from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World! This is a Python web app using Django.")