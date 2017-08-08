import inspect

from django.conf.urls import url
from django.views.generic import UpdateView, DeleteView, DetailView, ListView

from trips import views

urlpatterns = [
    url(r'^cbv/$', views.CityList.as_view(), name='city_cbv_list'),
    url(r'^cbv/create/$', views.CityCreate.as_view(), name='city_cbv_create'),
    url(r'^cbv/update/(?P<pk>\d+)$', views.CityUpdate.as_view(), name='city_cbv_update'),
    url(r'^cbv/delete/(?P<pk>\d+)$', views.CityDelete.as_view(), name='city_cbv_delete'),
    url(r'^cbv/view/(?P<pk>\d+)$', views.CityView.as_view(), name='city_cbv_view'),
    url(r'^cbv/modify/(?P<pk>\d+)$', views.CityModify.as_view(), name='city_cbv_modify'),
    url(r'^cbv/query/$', views.CityQuery.as_view(), name='city_cbv_query'),
    url(r'^cbv/first/$', views.CityFirst.as_view(), name='city_cbv_first'),
    url(r'^cbv/home/$', views.CityHome.as_view(), name='city_cbv_home'),
    url(r'^fbv/$', views.city_list, name='city_fbv_list'),
    url(r'^fbv/create/$', views.city_create, name='city_fbv_create'),
    url(r'^fbv/update/(?P<pk>\d+)$', views.city_update, name='city_fbv_update'),
    url(r'^fbv/delete/(?P<pk>\d+)$', views.city_delete, name='city_fbv_delete'),
    url(r'^fbv/view/(?P<pk>\d+)$', views.city_view, name='city_fbv_view'),
    url(r'^fbv/modify/(?P<pk>\d+)$', views.city_modify, name='city_fbv_modify'),
    url(r'^fbv/query/$', views.city_query, name='city_fbv_query'),
    url(r'^fbv/first/$', views.city_first, name='city_fbv_first'),
    url(r'^fbv/home/$', views.city_home, name='city_fbv_home'),
]

all_classes = inspect.getmembers(views, inspect.isclass)
for c in all_classes:
    if 'City' not in c[0] or 'City' == c[0]:
        continue

    pkViews = [UpdateView, DeleteView, DetailView]
    parents = inspect.getmro(c[1])
    name = (('city_cbv_' + c[0]).replace('_City', '_')).lower()

    if c[0].endswith('List') and ListView in parents:
        urlpatterns.append(url(r'^cbv/$', c[1].as_view(), name=name))
    elif [i for i in pkViews if i in parents]:
        urlpatterns.append(url(r'^cbv/' + name.replace('city_cbv_', '') + '/(?P<pk>\d+)$', c[1].as_view(), name=name))
    else:
        urlpatterns.append(url(r'^cbv/' + name.replace('city_cbv_', '') + '/$', c[1].as_view(), name=name))

all_functions = inspect.getmembers(views, inspect.isfunction)
for f in all_functions:
    if 'city' not in f[0]:
        continue

    method_to_call = getattr(views, f[0])
    args = (inspect.getfullargspec(method_to_call)[0])
    name = ('city_fbv_' + f[0]).replace('_city_', '_')

    if '_list' in f[0]:
        urlpatterns.append(url(r'^fbv/$', method_to_call, name=name))
    elif 'pk' in args:
        urlpatterns.append(url(r'^fbv/' + name.replace('city_fbv_', '') + '/(?P<pk>\d+)$', method_to_call, name=name))
    else:
        urlpatterns.append(url(r'^fbv/' + name.replace('city_fbv_', '') + '/$', method_to_call, name=name))
