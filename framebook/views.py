from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    con = {}
    return render(request, "framebook/index.html", con)

def get_data(request):
    if request.method == "POST":
        if data in request:
            return HttpResponse(data);
    return HttpResponse("Nothing here..!!!")
