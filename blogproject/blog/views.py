from dataclasses import fields
from django.shortcuts import render
from django.template import TemplateSyntaxError
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from blog.models import Post

# Create your views here.
#def home(request):
#    return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields =['title','title_tag','body']