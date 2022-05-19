from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test_view(request):
    return HttpResponse('Testapp, test_view')

def to_do_view(request):
    return render(request,'todo.html')

    