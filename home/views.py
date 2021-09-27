from django.shortcuts import render
from datetime import date
import subprocess
import math
# Create your views here.

def home_page(request):
    today = date.today()
    pi = math.pi
    e = math.e
    current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    return render(request, "home.html", {"today":today, "pi":pi, "e":e, "current_machine_id":current_machine_id})