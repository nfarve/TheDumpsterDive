from django.conf.urls import patterns, url
from TheDive import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        


        
)

