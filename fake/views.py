from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):

    model = joblib.load("model.sav")
    
    lis =[]

    lis.append(request.GET['Price'])
    lis.append(request.GET['Tenure'])
    lis.append(request.GET['Property_Type'])
    lis.append(request.GET['Built_Up'])
    lis.append(request.GET['Furnishing'])
    lis.append(request.GET['Bedroom'])
    lis.append(request.GET['Bathroom'])
    lis.append(request.GET['Area'])


    ans = model.predict([lis])

    result2=""
    if ans==[1]:
        result2 = "1"
    elif ans==[0]:
        result2 = "0"
    else:
        return "Enter new data"


    return render(request,"result.html",{'result2':result2, 'lis':lis})