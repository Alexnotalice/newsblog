from django.shortcuts import render
import requests
# Create your views here.
def news():

    r = requests.get('http://api.mediastack.com/v1/news?access_key=212e9c74b6cf77879522202b4ebbbce5&country=us')

    





    