from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("This is home page")

def table(c,n):
	j=" "
	for i in range(1,11):
		j+="{} x {:02} = {:02} </br> ".format(n,i,n*i)
	return HttpResponse(j)

def details(c,name):
	Name='<h2> Name = {}</h2>'.format(name)
	return HttpResponse(Name)

def mytrail(request,name,age):
	data={'name':name,'age':age}
	return render(request,'userapp/mytrail.html',data)

def sample(request):
	return render(request,'userapp/demo.html')
def login(request):
	return render(request,'userapp/login.html')
def Reg(request):
	return render(request,'userapp/Reg.html')
def jas(request):
	return render(request,'userapp/jas.html')