from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import BlogPostModel
# Create your views here.

# login_required tells it you HAVE to log in
@login_required
def index(request):
    # this will filter out the information you want to show off and lets you itterate through it easily
    blog = BlogPostModel.objects.filter(userIDkey=request.user)

    context = \
        {
            'blog_list': blog
        }
    return render(request,'blogApp/index.html',context)
# this was used to redirect but it automatically does it if you have login redirect assigned
# def logIn(request):
#     return redirect('accounts/login')