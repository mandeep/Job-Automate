from django.shortcuts import render
from django.http import HttpResponseRedirect
from jobautomate.web_application import django_view
from .forms import NameForm, EmailForm, UploadForm, JobSearchForm
from .models import ResumeModel


def index(request):
    if request.method == 'POST':
        name_form = NameForm(request.POST)
        email_form = EmailForm(request.POST)
        upload_form = UploadForm(request.POST, request.FILES)
        job_search_form = JobSearchForm(request.POST)
        if name_form.is_valid() and email_form.is_valid() \
                and upload_form.is_valid() and job_search_form.is_valid():
            first_name = name_form.cleaned_data['first_name']
            last_name = name_form.cleaned_data['last_name']
            email = email_form.cleaned_data['email']
            resume = ResumeModel()
            what = job_search_form.cleaned_data['job_description']
            where = job_search_form.cleaned_data['job_location']
            django_view(what, where, first_name, last_name, email, resume)
            return HttpResponseRedirect('web_search/index.html')
    else:
        name_form = NameForm()
        email_form = EmailForm()
        upload_form = UploadForm()
        job_search_form = JobSearchForm()
    return render(request, 'web_search/index.html',
                  {'name_form': name_form, 'email_form': email_form,
                   'upload_form': upload_form, 'job_search_form': job_search_form})
