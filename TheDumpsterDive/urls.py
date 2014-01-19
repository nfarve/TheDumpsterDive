from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
from TheDive.models import Category, Page, User
admin.autodiscover()

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(User)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TheDumpsterDive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^TheDive/', include('TheDive.urls')),
    
)

if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
