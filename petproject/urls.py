from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'main.views.main', name='home'),
    # Examples:
    # url(r'^$', 'Book.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
