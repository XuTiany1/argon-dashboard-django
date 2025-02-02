# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import StudentForm
from .models import Student


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.

#     if request.method == "POST":
#         form = Student(request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = Student()
        
    try:


        load_template = request.path.split('/')[-1]  
        html_template = loader.get_template( load_template )
        
        if(load_template == "students.html"):
            form = Student.objects.all()
            context = {'form':form} 
            #print(form.query)

            return HttpResponse(html_template.render(context, request))

        context['segment'] = load_template
        

        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
