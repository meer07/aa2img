from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Aa2Img.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('cms.urls', namespace='cms')),
)
