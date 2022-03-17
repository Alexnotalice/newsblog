from django.urls import  path 
from . import views

urlpatterns = [
    #path('',views.home, name="home")
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
]