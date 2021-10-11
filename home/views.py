from django.shortcuts import render
from datetime import date
import subprocess
import math
# Create your views here.

def home_page(request):
    today = date.today()
    pi = math.pi
    e = math.e
    return render(request, "home.html", {"today":today, "pi":pi, "e":e})