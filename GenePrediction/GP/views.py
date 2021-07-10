from django.shortcuts import render

def home(request):
	return render(request,'GP/home.html')

def predict(request,username):
    return HttpResponse("You're voting on question %s" %username)