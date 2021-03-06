from django.conf.urls.defaults import patterns, include, url
import settings
from os import path as os_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suco.views.home', name='home'),
    # url(r'^suco/', include('suco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('suco.smart_selects.urls')),
    (r'^xls/$', 'suco.utils.save_as_xls'),
    (r'^$', 'suco.encuesta.views.index'),
    (r'^', include('suco.encuesta.urls')),
)

urlpatterns += staticfiles_urlpatterns() 

#if settings.DEBUG:
#    urlpatterns += patterns('',
#                            (r'^files/(.*)$', 'django.views.static.serve',
#                             {'document_root': os_path.join(settings.MEDIA_ROOT)}),
#                           )
