from django.conf.urls import url

from . import views
#app_name = 'brain'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/$',{'template_name': 'brain/result.html'}, name='result'),
    url(r'^test/$', views.test, name='test'),
]
