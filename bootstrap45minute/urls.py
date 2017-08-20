from django.conf.urls import url
from bootstrap45minute import views

urlpatterns = [

    # Home Page url:
    url(r'^home/$', views.Bootstrap45minuteHome, name="Bootstrap45minuteHome"),

]
