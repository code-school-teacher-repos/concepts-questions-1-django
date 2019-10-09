from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(f'<h2>You Have Reached the Landing Page!</h2>')
