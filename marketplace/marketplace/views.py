# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
#    return HttpResponse("Hello World! I'm Home.")
    return render(request, 'home.html')

@login_required(login_url="/users/login/")
def my_account(request):
#    return HttpResponse("My Account Page.")
    return render(request, 'my_account.html')