from django.conf.urls import url
from blogs.views import blogpost_list, blogpost_detail, add_blogpost,\
                         update_blogpost
urlpatterns = [
    url(r'^$', blogpost_list, name = 'BlogPost List'),
    url(r'^detail-(?P<slug>\d+)/', blogpost_detail, name = 'BlogPost Detail'),
    url(r'new-blogpost/', add_blogpost, name = 'Add BlogPost'),
    url(r'update-blogpost-(?P<slug>\d+)/', update_blogpost,
                 name = 'Update BlogPost')
]
