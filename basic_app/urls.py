from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'


urlpatterns= [
    url(r'^$',views.SchoolListview.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailview.as_view(),name = 'detail' ),
    url(r'^create/$', views.SchoolCreateview.as_view(), name= 'create' ),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateview.as_view(),name = 'update' ),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteview.as_view(),name = 'delete' ),



]


