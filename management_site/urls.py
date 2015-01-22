from django.conf.urls import patterns, url
from management_site import views

urlpatterns = patterns(
    '',
    url(r'changevariables/', views.change_variables, name='change_variables'),
    url(r'$', views.index, name='index'),
)