from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    index_file = open('static/index.html').read()
    return HttpResponse(index_file)