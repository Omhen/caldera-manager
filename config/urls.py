from django.conf.urls import patterns, include, url
from management_site import views


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'eye.views.home', name='home'),

    url(r'^', include('management_site.urls')),
)

