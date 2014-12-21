from django.conf.urls import patterns, include, url
from django.contrib import admin

from MyJiaxing.views import hello, current_datetime, hours_ahead
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jiaxing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^hello/', hello),
    (r'^current_time$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead)
)
