from django.shortcuts import render
from .forms import *
from django.http import HttpRequest
from django.shortcuts import redirect
# Create your views here.


def render_home(request):
    return render(request = request, template_name = "happy_app/button1.html")

def render_reg(request:HttpRequest):
    if request.method == "POST":
            form = RegForm(request.POST) 
            if form.is_valid():
                form.save() 
                return redirect('buttons')
    else:
        form = RegForm()
    return render(request = request, template_name = "happy_app/happy.html", context = {"form": form})