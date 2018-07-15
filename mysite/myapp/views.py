from django.shortcuts import render
from django.http import HttpResponse,Http404
# from django.template import template
import datetime
# Create your views here.
def index(request):
	return render(request,'current_datetime.html',{'current_date':['red','yellow','bule','black']})

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	assert False
	html = "<html><body>In %s hour(s),it will be %s..</body></html>" % (offset,dt)
	return HttpResponse(html)