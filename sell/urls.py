from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$','sell.views.sellmainpage'),
    url(r'^product/','sell.views.detail', name='product_detail'),
]
