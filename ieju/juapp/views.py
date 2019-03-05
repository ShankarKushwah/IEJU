from django.shortcuts import render, HttpResponse


def index(request):
	return HttpResponse("<h1>Hello World.</h1>")

def about(request):
	return HttpResponse("<h1>About Page</h1>")

def semester(request):
	return HttpResponse("<h1>semester page</h1>")
