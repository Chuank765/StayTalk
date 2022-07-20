from django.shortcuts import render, redirect
from forms import PostForm
from models import BoardUnit
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
    if page_index == None:
        page = 0
        board_units = BoardUnit.objects.order_by('-id')[:page_size]
    elif page_index == 'prev':
        start = (page - 1)
        if start > 0:
            board_units = BoardUnit.objects.order_by('-id')[start: (start + page_size)]
            page -= 1
    elif page_index == 'next':
        start = (page + 1) * page_size
        if start < datasize:
            board_units = BoardUnit.objects.order_by('-id')[start:(start + page_size)]
            page += 1
    current_page = page + 1
    return render(request, 'index.html', locals())