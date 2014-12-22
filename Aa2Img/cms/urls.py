__author__ = 'naoya-kaige'
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Aa2Img.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^aa2img/', views.change, name='aa2img'),
)