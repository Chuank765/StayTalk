from django.shortcuts import render, redirect
from footprint.forms import PostForm
from footprint.models import Board
from django.contrib.auth import authenticate
from django.contrib import auth
import math


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
		  unit = Board.objects.create(base_name=name, base_gender=gender, base_subject=subject, base_mail=mail, base_web=web, base_content=content, base_response='')
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

def delete(request, board_id=None, delete_type=None):
	unit = Board.objects.get(id=board_id)
	if delete_type == 'del':
		unit.delete()
		return redirect('/adminmain/')
	return render(request, "delete.html", locals())