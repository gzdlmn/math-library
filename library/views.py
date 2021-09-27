from django.shortcuts import render,redirect,reverse
from . forms import FourOperationsForm,TrigonometryForm,QuadraticEquationsForm,FactorialForm,SquareRootForm,ExponentsForm,\
    LogarithmForm,EbobForm,DegreeRadianForm,CircleForm,RectangleForm,CubeForm,CylinderForm,SphereForm
from django.http import HttpResponseRedirect
import math



# Create your views here.

def four_operations(request):
    answer = 0
    form = FourOperationsForm(request.POST or None)
    if form.is_valid():
        first_field = form.cleaned_data.get('first_field')
        select = form.cleaned_data.get('select')
        second_field = form.cleaned_data.get('second_field')
        if select == "+":
            answer = float(first_field)+float(second_field)
            return render(request, "fouroperations.html", {"answer": answer})
        elif select == "-":
            answer = float(first_field)-float(second_field)
            return render(request, "fouroperations.html", {"answer": answer})
        elif select == "*":
            answer = float(first_field)*float(second_field)
            return render(request, "fouroperations.html", {"answer": answer})
        elif select == "/":
            answer = float(first_field)/float(second_field)
            return render(request, "fouroperations.html", {"answer": answer})
        else:
            return render(request, "fouroperations.html")
    return render(request, "fouroperations.html", {"form":form, "answer":answer})

#a=cos, b=sin, c=tan, d=cot, e=sec, f=cosec
def trigonometry_operations(request):
    form = TrigonometryForm(request.POST or None)
    if form.is_valid():
        value = form.cleaned_data.get("value")
        value = float(value)
        if value != 0:
            a = math.sin(value)
            a = round(a,4)
            adegree = math.sin(math.radians(value))
            adegree = round(adegree, 3)
            b= math.cos(value)
            b = round(b,4)
            bdegree = math.cos(math.radians(value))
            bdegree = round(bdegree,3)
            c = math.tan(value)
            c = round(c,4)
            cdegree = math.tan(math.radians(value))
            cdegree = round(cdegree,3)
            if value == 90 or value == 270:
                cdegree = ""
            d = 1/(math.tan(value))
            d = round(d,4)
            ddegree =  1/(math.tan(math.radians(value)))
            ddegree = round(ddegree,3)
            if value == 180 or value == 360:
                ddegree = ""
            e = 1/(math.cos(value))
            e = round(e,4)
            edegree = 1 / (math.cos(math.radians(value)))
            edegree = round(edegree,3)
            if value == 270:
                edegree = ""
            f = 1/(math.sin(value))
            f = round(f,4)
            fdegree = 1/(math.sin(math.radians(value)))
            fdegree = round(fdegree,3)
            if value == 180:
                fdegree = ""
            return render(request, "trigonometry.html", {"a":a, "b":b, "c":c, "d":d, "e":e, "f":f,
                                                         "adegree":adegree, "bdegree":bdegree, "cdegree":cdegree,
                                                         "ddegree":ddegree, "edegree":edegree, "fdegree":fdegree, "value":value})
        elif value == 0:
            a = int(math.sin(value))
            adegree = math.sin(math.radians(value))
            adegree = round(adegree, 3)
            b = int(math.cos(value))
            bdegree = math.cos(math.radians(value))
            bdegree = round(bdegree, 3)
            c = int(math.tan(value))
            cdegree = math.tan(math.radians(value))
            cdegree = round(cdegree, 3)
            d = ""
            ddegree = ""
            e = int(1/(math.cos(value)))
            edegree = 1/(math.cos(math.radians(value)))
            edegree = round(edegree,3)
            f = ""
            fdegree = ""
            return render(request, "trigonometry.html", {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f,
                                                         "adegree":adegree, "bdegree":bdegree, "cdegree":cdegree,
                                                         "ddegree":ddegree, "edegree":edegree, "value": value})
    return render(request, "trigonometry.html", {"form":form})

#to solve quadratic equations
def all_functions(request):
    quadraticequationsform = QuadraticEquationsForm(request.POST or None)
    factorialform = FactorialForm(request.POST or None)
    squarerootform = SquareRootForm(request.POST or None)
    exponentsform = ExponentsForm(request.POST or None)
    logarithmform = LogarithmForm(request.POST or None)
    ebobform = EbobForm(request.POST or None)
    degreeradianform = DegreeRadianForm(request.POST or None)
    if quadraticequationsform.is_valid():
        a = quadraticequationsform.cleaned_data.get("a")
        b = quadraticequationsform.cleaned_data.get("b")
        c = quadraticequationsform.cleaned_data.get("c")
        disc = ((b**2)-(4*a*c))**0.5
        if a != 0:
            x1 = (-b+(disc))/(2*a)
            x2 = (-b-(disc))/(2 * a)
        elif a == 0:
            x1 = "the equation is not quadratic"
            x2 = "the equation is not quadratic"
        return render(request, "functions.html", {"x1":x1, "x2":x2})
    elif factorialform.is_valid():
        value = factorialform.cleaned_data.get("value")
        value = int(value)
        if value >= 0:
            a = math.factorial(value)
        else:
            a="Sorry, factorial does not exist for negative numbers"
        return render(request, "functions.html", {"a":a})
    elif squarerootform.is_valid():
        valuesquare = squarerootform.cleaned_data.get("valuesquare")
        valuesquare = float(valuesquare)
        if valuesquare >=0 :
            result = math.sqrt(valuesquare)
        else:
            result = "Negative numbers don't have real square roots since a square is either positive or 0."
        return render(request, "functions.html", {"result":result})
    elif exponentsform.is_valid():
        expo1 = exponentsform.cleaned_data.get("expo1")
        expo1 = float(expo1)
        expo2 = exponentsform.cleaned_data.get("expo2")
        expo2 = float(expo2)
        resultexpo = math.pow(expo1,expo2)
        return render(request, "functions.html", {"resultexpo":resultexpo})
    elif logarithmform.is_valid():
        loga = logarithmform.cleaned_data.get("loga")
        logb = logarithmform.cleaned_data.get("logb")
        if float(loga)>0 and float(logb)>0:
            resultlog = math.log(logb,loga)
            return render(request, "functions.html", {"resultlog":resultlog})
    elif ebobform.is_valid():
        eboba = ebobform.cleaned_data.get("eboba")
        ebobb = ebobform.cleaned_data.get("ebobb")
        if int(eboba)>0 and int(ebobb)>0:
            resultebob = math.gcd(eboba,ebobb)
            return render(request, "functions.html", {"resultebob":resultebob})
    elif degreeradianform.is_valid():
        selectdegreeradian = degreeradianform.cleaned_data.get("selectdegreeradian")
        degreeorradian = degreeradianform.cleaned_data.get("degreeorradian")
        if selectdegreeradian == "radian":
            resultdegreeorradian = math.degrees(degreeorradian)
        elif selectdegreeradian == "degree":
            resultdegreeorradian = math.radians(degreeorradian)
        elif selectdegreeradian == "seçiniz":
            resultdegreeorradian = "select degree or radian"
        return render(request, "functions.html", {"resultdegreeorradian":resultdegreeorradian})
    return render(request, "functions.html", {"quadraticequationsform":quadraticequationsform, "factorialform":factorialform,
                                              "squarerootform":squarerootform, "exponentsform":exponentsform, "logarithmform":logarithmform,
                                              "ebobform":ebobform, "degreeradianform":degreeradianform})

def geometry(request):
    circleform = CircleForm(request.POST or None)
    rectangleform = RectangleForm(request.POST or None)
    cubeform = CubeForm(request.POST or None)
    cylinderform = CylinderForm(request.POST or None)
    sphereform = SphereForm(request.POST or None)
    if circleform.is_valid():
        r = circleform.cleaned_data.get("r")
        if r > 0:
            circlearea = (math.pi)*(r**2)
            circlearea = round(circlearea, 3)
            circleenvironment = 2*(math.pi)*r
            circleenvironment = round(circleenvironment, 3)
        elif r <= 0:
            circlearea = "None"
            circleenvironment = "None"
        return render(request, "geometry.html", {"circlearea":circlearea, "circleenvironment":circleenvironment})
    elif rectangleform.is_valid():
        recta = rectangleform.cleaned_data.get("recta")
        rectb = rectangleform.cleaned_data.get("rectb")
        if recta > 0 and rectb >0:
            arearectangle = recta*rectb
            rectangleenvironment = 2*recta*rectb
        elif recta <= 0 or rectb<= 0:
            arearectangle = "None"
            rectangleenvironment = "None"
        return render(request, "geometry.html", {"arearectangle":arearectangle, "rectangleenvironment":rectangleenvironment})
    elif cubeform.is_valid():
        cubea = cubeform.cleaned_data.get("cubea")
        if cubea > 0:
            areacube = 6*cubea*cubea
            cubevolume = cubea*cubea*cubea
        elif cubea <= 0:
            areacube = "None"
            cubevolume = "None"
        return render(request, "geometry.html", {"areacube":areacube, "cubevolume":cubevolume})
    elif cylinderform.is_valid():
        cylinderr = cylinderform.cleaned_data.get("cylinderr")
        cylinderh = cylinderform.cleaned_data.get("cylinderh")
        if cylinderr > 0 and cylinderh > 0:
            cylinderbasearea = (math.pi)*cylinderr*cylinderr
            cylinderbasearea = round(cylinderbasearea, 3)
            cylinderlateralsurface = 2*math.pi*cylinderr*cylinderh
            cylinderlateralsurface = round(cylinderlateralsurface, 3)
            cylindertotalarea = (2*math.pi*cylinderr*cylinderh)+(2*math.pi*cylinderr*cylinderr)
            cylindertotalarea = round(cylindertotalarea, 3)
            cylindervolume = math.pi*cylinderr*cylinderr*cylinderh
            cylindervolume = round(cylindervolume, 3)
        elif cylinderr <= 0 or cylinderh <= 0:
            cylinderbasearea = "None"
            cylinderlateralsurface = "None"
            cylindertotalarea = "None"
            cylindervolume = "None"
        return render(request, "geometry.html", {"cylinderbasearea":cylinderbasearea, "cylinderlateralsurface":cylinderlateralsurface,
                                                 "cylindertotalarea":cylindertotalarea, "cylindervolume":cylindervolume})
    elif sphereform.is_valid():
        spherer = sphereform.cleaned_data.get("spherer")
        if spherer > 0:
            totalsurfacesphere = 4*math.pi*spherer*spherer
            totalsurfacesphere = round(totalsurfacesphere, 3)
            totalvolumesphere = (4/3)*(math.pi)*spherer*spherer
            totalvolumesphere = round(totalvolumesphere, 3)
        elif spherer <=0 :
            totalsurfacesphere = "None"
            totalvolumesphere = "None"
        return render(request, "geometry.html", {"totalsurfacesphere":totalsurfacesphere, "totalvolumesphere":totalvolumesphere})
    return render(request, "geometry.html", {"circleform":circleform, "rectangleform":rectangleform, "cubeform":cubeform, "cylinderform":cylinderform,
                                             "sphereform":sphereform})