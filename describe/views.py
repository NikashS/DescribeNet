from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import random
import requests

from .models import Description

wnids = [
    ('n01443537', 'Goldfish'),
    ('n01484850', 'Great White Shark'),
    ('n01498041', 'Stingray'),
    ('n01986214', 'Hermit Crab'),
    ('n02051845', 'Pelican'),
    ('n02840245', 'Binder'),
    ('n02877765', 'Bottlecap'),
    ('n02883205', 'Bow Tie'),
    ('n02980441', 'Castle'),
    ('n02999410', 'Chain'),
    ('n02084071', 'Dog'),
    ('n03196217', 'Digital Clock'),
    ('n03255030', 'Dumbbell'),
    ('n03272010', 'Electric Guitar'),
    ('n03345487', 'Fire Truck'),
    ('n03445777', 'Golf Ball'),
    ('n03544143', 'Hourglass'),
    ('n03590841', 'Jack-O-Lantern'),
    ('n03759954', 'Microphone'),
    ('n03933933', 'Pier'),
    ('n03982430', 'Pool Table'),
    ('n04090263', 'Rifle'),
    ('n04125021', 'Safe'),
    ('n04194289', 'Ship'),
    ('n04285008', 'Sports Car'),
    ('n04557648', 'Water Bottle'),
    ('n07614500', 'Ice Cream'),
    ('n07873807', 'Pizza'),
    ('n15075141', 'Toilet Paper'),
]

def _get_urls():
    wnid, class_name = random.choice(wnids)
    url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=' + wnid
    page = requests.get(url)
    urls = page.content.decode("utf-8").split('\n')[:8]
    return (class_name, wnid, urls)

def login(request):
    return render(request, 'describe/login.html')

def login_submit(request):
    try:
        name = request.POST['name']
    except (KeyError):
        return login(request)

    username = name.replace(" ", "").lower()
    
    return HttpResponseRedirect(reverse('describe', args=(username,)))

def describe(request, username):
    class_name, wnid, urls = _get_urls()
    context = {
        'class_name': class_name,
        'username': username,
        'wnid': wnid,
        'first_urls': urls[:4],
        'last_urls': urls[4:8],
        'error_message': None,
    }
    return render(request, 'describe/describe.html', context)

def describe_submit(request):
    try:
        description_text = request.POST['description']
        wnid = request.POST['wnid']
        class_name = request.POST['class_name']
        username = request.POST['username']
    except (KeyError):
        return describe(request)
    
    description = Description(class_id=wnid, class_name=class_name, description_text=description_text, username=username)
    description.save()
    return HttpResponseRedirect(reverse('describe', args=(username,)))
