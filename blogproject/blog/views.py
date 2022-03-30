from dataclasses import fields
from django.shortcuts import render
from django.template import Context, TemplateSyntaxError
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post
from django.urls import reverse_lazy
from .forms import PostForm
import requests

# Create your views here.
#def home(request):
#    return render(request,'home.html',{})

# class HomeView(ListView):
#     model = Post    
#     template_name = 'home.html'
#     ordering = ['-id']

def web_data():
        r = requests.get('http://api.mediastack.com/v1/news?access_key=212e9c74b6cf77879522202b4ebbbce5&keywords =basketball&countries=us')
        req = r.json()
        data = req['data']
        title = []
        description = []
        image = []
        url = []
        count=0
        for i in data:              
            title.append(i['title'])
            description.append(i['description'])
            image.append(i['image'])
            url.append(i['url'])
            count+=1
            if count == 3:
                break

    
        news = zip(title, description, image, url)  
        return news

new=web_data()
def HomeView(request):
	model = Post.objects.all()
 
	context = {'object_list':model,'news':new}    
	return render(request, 'home.html',context)


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
     
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields =['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')