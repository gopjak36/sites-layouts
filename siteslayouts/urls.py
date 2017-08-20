from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # Bootstrap45minute urls:
    url(r'^bootstrap45minute/', include('bootstrap45minute.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
