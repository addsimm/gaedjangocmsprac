from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:

                       # url(r'^gaedjangocmsprac/', include('gaedjangocmsprac.foo.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       #url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/js/tinymce/'}),
                       url(r'display_flatpage', 'cmspracapp.views.display_flatpage', name='display_flatpage'),
                       url(r'create_flatpage', 'cmspracapp.views.create_flatpage', name='create_flatpage'),
                       url(r'^/*', 'cmspracapp.views.home', name='home'),
                       )
