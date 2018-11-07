from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^index/$", views.index),
    url(r"^weather/([a-z]+)/(\d{4})/$", views.weather),
    url(r"^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})", views.weather2)
]
