# letschat_app/urls.py
from django.urls import path
from .views import index,roomname
app_name='chatapp'
urlpatterns = [
    path('chat/', index, name="index"),
    path('chat/<str:name>/', roomname, name='room')
]