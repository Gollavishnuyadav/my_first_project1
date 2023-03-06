from django.shortcuts import render
from django.http import HttpResponse
def sample(request):
    return HttpResponse("<button><labe>We are Learning django</label><h1><marquee>django is a framework</h1></marquee><button>")

def sample1(request):
    return HttpResponse("<table><labe>click</label><button>Click</button>")
