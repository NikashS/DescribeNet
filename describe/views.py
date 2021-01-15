from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import random
import requests
from lxml import html

from .models import Description
from .static.wnids import wnids

def _get_urls():
    wnid, class_name = random.choice(wnids)

    url = 'http://deep.cs.virginia.edu/data/imagenet256/train/' + wnid + '/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    picture_names = tree.xpath('//a/text()')
    urls = [url + picture_name for picture_name in picture_names[20:28]]
    return (class_name, wnid, urls)

def login(request):
    return render(request, 'describe/login.html')

def login_submit(request):
    try:
        name = request.POST['name']
    except (KeyError):
        return login(request)

    username = name.replace(" ", "").replace("-", "").lower()
    
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
