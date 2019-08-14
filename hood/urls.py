from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
  # url(r'^accounts/profile/$',views.profile,name = 'profile'),
 
   url('^$',views.home,name ='home'),
   url(r'^hood/$', views.add_hood, name='add_hood'),
   url(r'register',views.register,name= 'signup'),
   #url(r'^join(?P<neighbourhood_id>\d+)',views.join, name='join'),
   url(r'^leave/(?P<neighbourhood_id>\d+)',views.leave, name='leave'),
   url(r'^one_hood(?P<neighbourhood_id>\d+)',views.hood, name='hood'),
   url(r'^upload/$', views.upload_business, name='upload_business'),
 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)