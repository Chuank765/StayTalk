from django.shortcuts import render, redirect
from footprint.forms import PostForm
from footprint.models import Board
from django.contrib.auth import authenticate
from django.contrib import auth
import math

def login(request):
	messages = ''
	if request.method == 'POST':
		name = request.POST['username'].strip()
		password = request.POST['passwd']
		user1 = authenticate(username=name, password=password)
		if user1 is not None:
			if user1.is_active:
				auth.login(request, user1)
				return redirect('/adminmain/')
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())

def logout(request):
	auth.logout(request)
	return redirect('/index/')