from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test_view(request):
    return HttpResponse('Testing, testing, 1-2-3.')