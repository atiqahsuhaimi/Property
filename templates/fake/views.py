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


    Price=request.GET['Price']
    Tenure=request.GET['Tenure']
    Property_Type=request.GET['Property_Type']
    Built_Up=request.GET['Built_Up']
    Furnishing=request.GET['Furnishing']
    Bedroom=request.GET['Bedroom']
    Bathroom=request.GET['Bathroom']
    Area=request.GET['Area']
    lis.append(Price)
    lis.append(Tenure)
    lis.append(Property_Type)
    lis.append(Built_Up)
    lis.append(Furnishing)
    lis.append(Bedroom)
    lis.append(Bathroom)
    lis.append(Area)

    

    ans = model.predict([lis])

    result2=ans
    if ans==[1]:
        result2 = "1"
    elif ans==[0]:
        result2 = "0"
    else:
        return "Enter new data"


    return render(request,"result.html",{'result2':result2, 'lis':lis})

 