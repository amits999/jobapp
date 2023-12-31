from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

# Create your views here.
def hello(request):
    template = loader.get_template('hello.html')
    context = {}
    return HttpResponse(template.render(context, request))

job_title = [
    'Job1 Title',
    'Job2 Title',
    'Job3 Title',
]

job_desc = [
    'Job1 Description',
    'Job2 Description',
    'Job3 Description',
]

def display_jobs(request):
    my_str = '<ul>'
    for j in job_title:
        job_id = job_title.index(j)
        my_str += f'<li> <a href= {reverse("jobs_detail", args=(job_id,))}> {j}</li>'
    my_str += '</ul>'

    return HttpResponse(my_str)

def job_detail_page(request, id):
    try:
        if id == 0:
            return redirect(reverse('main_page'))
        
        return_html = f'<h1>{job_title[id]}</h1> <h3>{job_desc[id]}</h3>'
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound('<h2>Page Not Found</h2>')