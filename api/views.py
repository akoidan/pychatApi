from django.shortcuts import render, render_to_response

# Create your views here.
import requests
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods

from django.conf import settings

from api.models import UploadedFile


@require_http_methods('GET')
def notify(request):
	token = request.GET.get('token', False)
	if token != getattr(settings, "PUSHBULLET_PARAM"):
		raise Http404
	pushbullet("User has clicked on the link", "POE")
	return HttpResponse("User has been notified", content_type='text/plain')



@require_http_methods(['POST'])
def upload_file(request):
	"""
	POST only, validates email during registration
	"""
	uf = UploadedFile(file=request.FILES['file'])
	uf.save()
	return HttpResponse(uf.file.url, content_type='text/plain')



def pushbullet(data, title):
	resp = requests.post('https://api.pushbullet.com/v2/pushes', json={
		'body': data,
		'type': 'note',
		'title': title
	}, headers={
		'Access-Token': getattr(settings, "PUSHBULLET_TOKEN"),
		'Content-Type': 'application/json'
	})
	if resp.status_code != 200:
		raise Exception(resp.content)

@require_http_methods('GET')
def valentine(request):
	"""
	Login or logout navbar is creates by means of create_nav_page
	@return:  the x intercept of the line M{y=m*x+b}.
	"""
	return render_to_response('valentine.html')


@require_http_methods('GET')
def birthday25(request):
	"""
	Login or logout navbar is creates by means of create_nav_page
	@return:  the x intercept of the line M{y=m*x+b}.
	"""
	return render_to_response('birthday.html')


@require_http_methods('GET')
def start_valentine(request):
	"""
	Login or logout navbar is creates by means of create_nav_page
	@return:  the x intercept of the line M{y=m*x+b}.
	"""
	return render_to_response('startValentine.html')

@require_http_methods('GET')
def start_new_year(request):
	"""
	Login or logout navbar is creates by means of create_nav_page
	@return:  the x intercept of the line M{y=m*x+b}.
	"""
	return render_to_response('startNewYear.html')


@require_http_methods('GET')
def continue_new_year(request):
	"""
	Login or logout navbar is creates by means of create_nav_page
	@return:  the x intercept of the line M{y=m*x+b}.
	"""
	return render_to_response('continueNewYear.html')
