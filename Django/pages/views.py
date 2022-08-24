from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
# function-based view - described in chapter 2
# def homepageview(request):
# return HttpResponse("Hello, World!")


# Class-based view - replaced the function view above
#class HomePageView(TemplateView):
    #template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
