"""pychatApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from api.views import start_valentine, valentine, notify, continue_new_year, birthday25, upload_file, galina_1, \
	galina_2, galina_3
from pychatApi import settings

urlpatterns = [
	url(r'^toMyDearGirlFriend', start_valentine),
	url(r'^ILoveYou', valentine, name='continue_valentine'),
	url(r'^galina_1', galina_1, name='galina_1'),
	url(r'^galina_2', galina_2, name='galina_2'),
	url(r'^galina_3', galina_3, name='galina_3'),
	url(r'^notify$', notify),
	url(r'^25', start_valentine),
	url(r'^HappyNewYear$', continue_new_year, name='continue_new_year'),
	url(r'^HappyBirthday', birthday25, name='continue_birthday'),
	url(r'^upload_file', upload_file),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
