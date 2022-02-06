from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Memes


def home(request):
    url = 'https://api.imgflip.com/get_memes'
    response =  requests.get(url)
    data = response.json()
    status = data['success']
    if status:
        dt = data['data']
        bt = dt['memes']
        for i in bt:
            meme_data= Memes(
                id = i['id'],
                name=i['name'],
                url =i['url']
            )
            meme_data.save()
        mems = Memes.objects.all()
        return render(request, 'index.html',{'mems':mems})
    else:
        return HttpResponse("Error while fatching data!!!")
