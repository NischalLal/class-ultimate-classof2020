from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from members.views import member_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', member_list, name = 'Member List Home'),
    url(r'^members/', include('members.urls')),
    url(r'^blog/', include('blogs.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)