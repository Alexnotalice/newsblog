from dataclasses import fields
from django.shortcuts import render
from django.template import Context, TemplateSyntaxError
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post
from django.urls import reverse_lazy
from .forms import PostForm,EditForm
import requests

# Create your views here.
#def home(request):
#    return render(request,'home.html',{})



# def web_data():
#         r = requests.get('http://api.mediastack.com/v1/news?access_key=f24ef91f76da924b999bb246fa72d85a&countries=us')
#         req = r.json()
#         data = req['data']
#         title = []
#         description = []
#         image = []
#         url = []
#         count=0
#         for i in data:              
#             title.append(i['title'])
#             description.append(i['description'])
#             image.append(i['image'])
#             url.append(i['url'])
#             count+=1
#             if count == 3:
#                 break

    
#         newsapi = zip(title, description, image, url)  
        
#         #news = zip(title, description, url)  
#         return newsapi

# newapi=web_data()
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    fields='__all__'
	# model = Post.objects.all()
 
	# context = {'object_list':model,'news':newapi}    
	# return render(request, 'home.html',context)

  


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    fields =['title','title_tag','author','body']
    template_name = 'add_post.html'
    #form_class = PostForm
     
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'    
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')