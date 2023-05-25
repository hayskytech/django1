from django.shortcuts import render

from django.http import HttpResponse

def home(request):
	# return HttpResponse("<h1>Hello world<h1>")
	return render(request, "home.html")



def about(request):
	# return HttpResponse("<h1>About us<h1>")
	return render(request, "about.html")