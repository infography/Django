from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect,HttpResponseNotFound
from fpickapp.models import *
from fpickcart.models import * 
from fpickapp.forms import UserForm,LoginForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def home(request):
	queryset = Computer.objects.all()
	context_dict = {'items':queryset,'user':request.user}
	return render(request,'home.html',context_dict)

def computer_peripherials(request,topic):
	items = Computer.objects.all()
	context_dict = {'items':items}
	return render(request,'item_list.html',context_dict)

def computer_catalog(request):
	items = Computer.objects.all()
	context_dict = {'items':items}
	return render(request,'catalog.html',context_dict)

def laptop_catalog(request):
	queryset = Computer.objects.filter(computer_type__name__iexact='laptop')
	context_dict = {'items':queryset}
	return render(request,'catalog.html',context_dict)

def desktop_catalog(request):
	queryset = Computer.objects.filter(computer_type__name__iexact='desktop')
	print 'hello---------------'
	context_dict = {'items':queryset}
	return render(request,'catalog.html',context_dict)

def computer_by_brand(request,bname):
	items = Computer.objects.filter(brand__brand_name=bname)
	context_dict={'items':items,'bname':bname}
	return render(request,'item_list.html',context_dict)

def computer_detail(request,pk):
	items = Computer.objects.filter(pk=pk)
	context_dict = {'items':items}
	return render(request,'computer_detail.html',context_dict)



def create_user(request):

	if request.method == 'POST':
		form = UserForm(request.POST)
		
		if form.is_valid():
			# email = form.cleaned_data['email']
			# subject = 'FirstPick account created'
			# message = 'Welcome to FirstPick, go shopping online now!!!!'
			# sender = 'infymee@gmail.com'
			# send_mail(subject, message,sender,[email])
			form.save()
			return HttpResponseRedirect('/home/')

	else:
		form = UserForm()
	return render(request,'create_account.html',{'forms':form})

def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			print email,'-----------------'
			password = request.POST['password']
			# username=request.POST['username']
			# user = authenticate(username=username,email=email, password=password)
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponseNotFound('<h1>INVALID LOGIN</h1>')
	else:
		form = LoginForm()
		return render(request,'login_page.html',{'forms':form})

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/home/')

def check(request):
	session = request.session
	print session
	return HttpResponse(session)

	








	
