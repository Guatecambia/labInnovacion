from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

def index():
    return HttpResponse("Hello, world. You're at the polls index.")