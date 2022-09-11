from django.shortcuts import render
def index(request):
   return render(request, 'chatapp/index.html')
def roomname(request, name):
        return render(request, 'chatapp/chatroom.html', {'roomname': name})
