from django.shortcuts import render

from django.http import HttpResponse

def home(request):
	x = request.GET.get('x','0'),
	y = request.GET.get('y','0'),
	z = int(x[0]) + int(y[0])
	
	data = {
		"age":20,
		"result" : z,
		"x" : x[0],
		"y" : y[0],
	}
	return render(request,"home.html",data)

def about(request):
	# return HttpResponse("<h1>About us<h1>")
	return render(request, "about.html")