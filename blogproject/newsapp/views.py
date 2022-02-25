from django.shortcuts import render
import requests


# Create your views here.
def web_data(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=212e9c74b6cf77879522202b4ebbbce5&keywords =basketball&countries=us')
    req = r.json()
    data = req['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description, image, url)
    return render(request, 'news.html', {'news':news})
