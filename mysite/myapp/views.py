from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html')

def mcgill(request):
	return render(request, 'mcgill.html')

def pacificacademy(request):
	return render(request, 'pacificacademy.html')

def projects(request):
	return render(request, 'projects.html')

def datastructure(request):
	return render(request, 'datastructure.html')

def designpattern(request):
	return render(request, 'designpattern.html')
