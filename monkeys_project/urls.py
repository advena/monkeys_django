from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monkeys_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^monkeys/', include('monkeys.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
