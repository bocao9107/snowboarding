from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$','snowboard.views.homepage'),
    url(r'^sking','snowboard.views.sking'),
    url(r'^snowboarding','snowboard.views.snowboarding'),
    url(r'^about','snowboard.views.about'),
    url(r'^activate','snowboard.views.activate'),
    url(r'^discussion','snowboard.views.discussion'),
    url(r'^sell','snowboard.views.sell'),
    
]
