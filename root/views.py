from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url

def createUrl(req):
    if req.method == 'POST':
        full_url = req.POST.get('full_url')
        obj = Url.create(full_url)
        return render(req, 'root/index.html', {
            'full_url': obj.full_url, 
            # 'short_url': 'https://gprojukti.com' + '/' +obj.short_url})
            'short_url': req.get_host() + '/' +obj.short_url})
    return render(req, 'root/index.html')


def routeToURL(reg, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        obj = None
    if obj:
        pass 
    return redirect(createUrl)