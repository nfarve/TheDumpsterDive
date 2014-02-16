from django.conf.urls import patterns, url
from TheDive import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),      
)

