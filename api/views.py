from django.shortcuts import render
from django.http import HttpResponse
#from api.serializers import TitleSerializer

#@api_view(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def search(request):
	return HttpResponse("JSON will be served here.")