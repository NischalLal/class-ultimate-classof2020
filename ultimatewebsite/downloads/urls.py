from django.conf.urls import url
from downloads.views import download_item, download_list

urlpatterns = [
        url(r'^(?P<id>\d+)/$', download_item, name = 'Download Item'),
        url(r'^all-downloads/', download_list, name = 'Download List'),

] 