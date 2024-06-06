from django.http import HttpResponse, FileResponse
from django.shortcuts import render


def home(request):

    return render(request, "index.html")