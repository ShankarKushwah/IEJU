from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='índex'),
    url(r'^about/$', views.about, name='about'),
    url(r'^semester/$', views.semester, name='semester'),

]
