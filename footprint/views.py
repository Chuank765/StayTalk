from django.shortcuts import render, redirect
from .forms import PostForm
from .models import BoardUnit
from django.contrib.auth import authenticate
from django.contrib import auth
import math

page = 0

def index(request, pageindex=None): 
	global page
	pagesize = 3
	boardall = models.BoardUnit.objects.all().order_by('-id')
	datasize = len(boardall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page = 0
		boardunits = BoardUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='prev':
		start = (page-1)*pagesize
		if start >= 0: 
			boardunits = BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page -= 1
	elif pageindex=='next':
		start = (page+1)*pagesize
		if start < datasize:
			boardunits = BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page += 1
	currentpage = page + 1
	return render(request, "index.html", locals())

def post(request):
	if request.method == "POST":
		postform = PostForm(request.POST)
		if postform.is_valid():
		  subject = postform.cleaned_data['boardsubject']
		  name =  postform.cleaned_data['boardname']
		  gender =  request.POST.get('boardgender', None)
		  mail = postform.cleaned_data['boardmail']
		  web =  postform.cleaned_data['boardweb']
		  content =  postform.cleaned_data['boardcontent']
		  unit = models.BoardUnit.objects.create(bname=name, bgender=gender, bsubject=subject, bmail=mail, bweb=web, bcontent=content, bresponse='')
		  unit.save()
		  message = '已儲存...'
		  postform = PostForm()
		  return redirect('/index/')	
		else:
		  message = '驗證碼錯誤！'	
	else:
		message = '標題、姓名、內容及驗證碼必須輸入！'
		postform = PostForm()
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

def adminmain(request, pageindex=None):
	global page
	pagesize = 3
	boardall = BoardUnit.objects.all().order_by('-id')
	datasize = len(boardall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page =0
		boardunits = BoardUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='prev':
		start = (page-1)*pagesize
		if start >= 0:
			boardunits = BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page -= 1
	elif pageindex=='next':
		start = (page+1)*pagesize
		if start < datasize:
			boardunits = BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page += 1
	elif pageindex=='ret':
		start = page*pagesize
		boardunits = BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
	else:
		unit = BoardUnit.objects.get(id=pageindex)
		unit.bsubject=request.POST.get('boardsubject', '')
		unit.bcontent=request.POST.get('boardcontent', '')
		unit.bresponse=request.POST.get('boardresponse', '')
		unit.save()
		return redirect('/adminmain/ret/')
	currentpage = page+1
	return render(request, "adminmain.html", locals())

def delete(request, boardid=None, deletetype=None):
	unit = BoardUnit.objects.get(id=boardid)
	if deletetype == 'del':
		unit.delete()
		return redirect('/adminmain/')
	return render(request, "delete.html", locals())
