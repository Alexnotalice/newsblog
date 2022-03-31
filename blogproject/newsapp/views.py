from django.shortcuts import render
from django.http import HttpResponse
import requests




# Create your views here.
def web_data(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=d19b1f74e4cc9f961a6d30afa7d2ed44&sources=en&sources=cnn,-bbc')
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
   
    newsapi = zip(title, description, image, url)  
     
  
    return render(request, 'cnews.html',{'newsapi':newsapi})

    
