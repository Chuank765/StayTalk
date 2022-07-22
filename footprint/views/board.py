from django.shortcuts import render, redirect
from footprint.models import Board
from django.contrib.auth import authenticate
from django.contrib import auth
import math


def index(request, page_index=None):
	global page
	page_size = 3
	board_all = Board.objects.all().order_by('-id')
	data_size = len(board_all)
	total_page = math.ceil(data_size / page_size)
	if page_index==None:
		page = 0
		boards = Board.objects.order_by('-id')[:page_size]
	elif page_index=='prev':
		start = (page-1)*page_size
		if start >= 0: 
			boards = Board.objects.order_by('-id')[start:(start+page_size)]
			page -= 1
	elif page_index=='next':
		start = (page+1)*page_size
		if start < data_size:
			boards = Board.objects.order_by('-id')[start:(start+page_size)]
			page += 1
	current_page = page + 1
	return render(request, "index.html", locals())

def adminmain(request, page_index=None):
	global page
	page_size = 3
	board_all = Board.objects.all().order_by('-id')
	data_size = len(board_all)
	totpage = math.ceil(data_size / page_size)
	if page_index==None:
		page =0
		boards = Board.objects.order_by('-id')[:page_size]
	elif page_index=='prev':
		start = (page-1)*page_size
		if start >= 0:
			boards = Board.objects.order_by('-id')[start:(start+page_size)]
			page -= 1
	elif page_index=='next':
		start = (page+1)*page_size
		if start < data_size:
			boards = Board.objects.order_by('-id')[start:(start+page_size)]
			page += 1
	elif page_index=='ret':
		start = page*page_size
		boards = Board.objects.order_by('-id')[start:(start+page_size)]
	else:
		board = Board.objects.get(id=page_index)
		board.base_subject=request.POST.get('board_subject', '')
		board.base_content=request.POST.get('board_content', '')
		board.base_response=request.POST.get('board_response', '')
		board.save()
		return redirect('/adminmain/ret/')
	currentpage = page+1
	return render(request, "adminmain.html", locals())