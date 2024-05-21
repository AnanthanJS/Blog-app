from django.views import generic, View
from django.shortcuts import render
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def my_about(request):
    return render(request, 'about.html')

def contact_me(request):
    return render(request, 'contact.html')