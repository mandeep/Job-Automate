from django.shortcuts import render
from jobautomate import run_script


def index(request):
    context = {}
    request.POST.get('job_title', 'job_location')
    if request.POST.get('run'):
        what = request.POST['job_title']
        where = request.POST['job_location']
        run_script(what, where)
    return render(request, 'web_search/index.html', context)
