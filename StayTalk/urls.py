"""StayTalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from footprint import views
from footprint.views import data, board, user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.index),
    path('index/', board.index),
    path('index/<str:page_index>/', board.index),
    path('post/', data.post),
    path('login/', user.login),
    path('logout/', user.logout),
    path('adminmain/', board.adminmain),
    path('adminmain/<str:page_index>/', board.adminmain),
    path('delete/<int:board_id>/', data.delete),
    path('delete/<int:board_id>/<str:delete_type>/', data.delete),
]