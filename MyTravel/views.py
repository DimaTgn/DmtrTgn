from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    name = "Dmitriy"
    context = {'name': 'Dave'}
    return render(request, 'home.html', context)