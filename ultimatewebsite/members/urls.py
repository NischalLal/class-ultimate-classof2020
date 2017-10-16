from django.conf.urls import url
from members.views import member_list, member_detail, add_member,\
                    update_member_info
urlpatterns = [
    url(r'^$', member_list, name = 'Member List'),
    url(r'^detail-(?P<pk>\d+)/', member_detail, name = 'Member Detail'),
    url(r'new-member/', add_member, name = 'Add Member'),
    url(r'update-member-(?P<pk>\d+)/', update_member_info,
                         name = 'Member Update')
]