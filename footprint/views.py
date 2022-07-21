from django.shortcuts import render, redirect
from .forms import PostForm
from .models import BoardUnit
from django.contrib.auth import authenticate
from django.contrib import auth
import math

page = 0

def index(request, page_index=None): 
	global page
	page_size = 3
	board_all = BoardUnit.objects.all().order_by('-id')
	data_size = len(board_all)
	total_page = math.ceil(data_size / page_size)
	if page_index==None:
		page = 0
		board_units = BoardUnit.objects.order_by('-id')[:page_size]
	elif page_index=='prev':
		start = (page-1)*page_size
		if start >= 0: 
			board_units = BoardUnit.objects.order_by('-id')[start:(start+page_size)]
			page -= 1
	elif page_index=='next':
		start = (page+1)*page_size
		if start < data_size:
			board_units = BoardUnit.objects.order_by('-id')[start:(start+page_size)]
			page += 1
	current_page = page + 1
	return render(request, "index.html", locals())

def post(request):
	if request.method == "POST":
		post_form = PostForm(request.POST)
		if post_form.is_valid():
		  subject = post_form.cleaned_data['board_subject']
		  name =  post_form.cleaned_data['board_name']
		  gender =  request.POST.get('board_gender', None)
		  mail = post_form.cleaned_data['board_mail']
		  web =  post_form.cleaned_data['board_web']
		  content =  post_form.cleaned_data['board_content']
		  unit = BoardUnit.objects.create(base_name=name, base_gender=gender, base_subject=subject, base_mail=mail, base_web=web, base_content=content, base_response='')
		  unit.save()
		  message = '已儲存...'
		  post_form = PostForm()
		  return redirect('/index/')	
		else:
		  message = '驗證碼錯誤！'	
	else:
		message = '標題、姓名、內容及驗證碼必須輸入！'
		post_form = PostForm()
	return render(request, "post.html", locals())

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

def adminmain(request, page_index=None):
	global page
	page_size = 3
	board_all = BoardUnit.objects.all().order_by('-id')
	data_size = len(board_all)
	totpage = math.ceil(data_size / page_size)
	if page_index==None:
		page =0
		board_units = BoardUnit.objects.order_by('-id')[:page_size]
	elif page_index=='prev':
		start = (page-1)*page_size
		if start >= 0:
			board_units = BoardUnit.objects.order_by('-id')[start:(start+page_size)]
			page -= 1
	elif page_index=='next':
		start = (page+1)*page_size
		if start < data_size:
			board_units = BoardUnit.objects.order_by('-id')[start:(start+page_size)]
			page += 1
	elif page_index=='ret':
		start = page*page_size
		board_units = BoardUnit.objects.order_by('-id')[start:(start+page_size)]
	else:
		unit = BoardUnit.objects.get(id=page_index)
		unit.base_subject=request.POST.get('board_subject', '')
		unit.base_content=request.POST.get('board_content', '')
		unit.base_response=request.POST.get('board_response', '')
		unit.save()
		return redirect('/adminmain/ret/')
	currentpage = page+1
	return render(request, "adminmain.html", locals())

def delete(request, board_id=None, delete_type=None):
	unit = BoardUnit.objects.get(id=board_id)
	if delete_type == 'del':
		unit.delete()
		return redirect('/adminmain/')
	return render(request, "delete.html", locals())
