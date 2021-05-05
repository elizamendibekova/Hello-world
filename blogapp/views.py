from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comments

# Create your views here.
def index(request):
	return HttpResponse("Это главная страница блога")



	