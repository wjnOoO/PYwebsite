from django.http import HttpResponse,Http404
import datetime

def hello(req):
    return HttpResponse("<h1>Hello World!</h1>")

def current_datetime(req):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s hour(s), it will be %s.</body></html>" %(offset,dt)
    return HttpResponse(html)

def ctime(req,num):
    try:
        num=int(num)
        num=str(num)
    except ValueError:
        raise Http404
    txt="url is [http://127.0.0.1:8000/time/%s/]" %num
    return HttpResponse(txt)