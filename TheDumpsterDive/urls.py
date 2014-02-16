from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


#the line below is giving an error message, commenting out for testing -- does this belong in views.py? -gk
#from TheDive.models import User, Category, Page 
admin.autodiscover()

#three lines below are giving an error message, commenting out for testing
#admin.site.register(Category) 
#admin.site.register(Page)
#admin.site.register(User)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheDumpsterDive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^$', include('TheDive.urls'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^TheDive/', include('TheDive.urls')),
    
)

if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
