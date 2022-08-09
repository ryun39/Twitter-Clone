from audioop import reverse
import re
from django.shortcuts import redirect, render
from django.views.generic import View

from .models import Tweet
from accountapp.models import User

class PostView(View):
    def get(self, request):
        if request.user.is_authenticated:
            u = User.objects.filter(username=request.user).values()
            
        return render(request, 'index.html', {'img': u[0]['Profile']})
    

class UserTweet(View):
    def post(self, request):
        data = request.POST
        
        new_t = Tweet()
        new_t.owner = request.user
        new_t.text  = data['feed']
        if request.FILES:
            new_t.img   = request.FIELS['img']

        new_t.save()

        return redirect('http://127.0.0.1:8000/post/')
