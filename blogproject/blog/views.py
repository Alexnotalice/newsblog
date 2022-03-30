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



def web_data():
        r = requests.get('http://api.mediastack.com/v1/news?access_key=212e9c74b6cf77879522202b4ebbbce5&keywords=covid&countries=us&limit=3')
        req = r.json()
        data = req['data']
        title = []
        description = []
        #image = []
        url = []
        count=0
        for i in data:              
            title.append(i['title'])
            description.append(i['description'])
            #image.append(i['image'])
            url.append(i['url'])
            count+=1
            if count == 3:
                break

    
        #news = zip(title, description, image, url)  
        #<img src="{{ image }}"  width="100%" height="225"
        news = zip(title, description, url)  
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