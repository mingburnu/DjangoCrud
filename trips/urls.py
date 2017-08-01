from django.conf.urls import url

from trips import views

urlpatterns = [
    url(r'^cbv/$', views.CityList.as_view(), name='city_cbv_list'),
    url(r'^cbv/add/$', views.CityCreate.as_view(), name='city_cbv_add'),
    url(r'^cbv/edit/(?P<pk>\d+)$', views.CityUpdate.as_view(), name='city_cbv_edit'),
    url(r'^cbv/delete/(?P<pk>\d+)$', views.CityDelete.as_view(), name='city_cbv_delete'),
    url(r'^cbv/view/(?P<pk>\d+)$', views.CityView.as_view(), name='city_cbv_view'),
    url(r'^cbv/modify/(?P<pk>\d+)$', views.CityModify.as_view(), name='city_cbv_modify'),
    url(r'^cbv/query/$', views.CityQuery.as_view(), name='city_cbv_query'),
    url(r'^cbv/first/$', views.CityFirst.as_view(), name='city_cbv_first'),
    url(r'^cbv/home/$', views.CityHome.as_view(), name='city_cbv_home'),
    url(r'^fbv/$', views.city_list, name='city_fbv_list'),
    url(r'^fbv/add/$', views.city_create, name='city_fbv_add'),
    url(r'^fbv/edit/(?P<pk>\d+)$', views.city_update, name='city_fbv_edit'),
    url(r'^fbv/delete/(?P<pk>\d+)$', views.city_delete, name='city_fbv_delete'),
    url(r'^fbv/view/(?P<pk>\d+)$', views.city_view, name='city_fbv_view'),
    url(r'^fbv/modify/(?P<pk>\d+)$', views.city_modify, name='city_fbv_modify'),
    url(r'^fbv/query/$', views.city_query, name='city_fbv_query'),
    url(r'^fbv/first/$', views.city_first, name='city_fbv_first'),
    url(r'^fbv/home/$', views.city_home, name='city_fbv_home'),
]
