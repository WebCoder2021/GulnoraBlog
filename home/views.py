from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.
def home(request):
    context = {}
    context['posts'] = Post.objects.all()[:3]

    return render(request,'index.html',context)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog.html'
    queryset = Post.objects.all()
    

 
 
class PostDetailView(DetailView):
    # specify the model to use
    model = Post
    template_name = 'blog-details.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context