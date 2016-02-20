from django.http import HttpResponse
from django.shortcuts import render
import jobautomate


def index(request):
    context = {}
    request.POST.get("job_title", "job_location")
    return render(request, 'web_search/index.html', context)
