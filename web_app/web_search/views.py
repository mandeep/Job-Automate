from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'web_search/index.html', context)
