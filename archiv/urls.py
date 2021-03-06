# generated by appcreator
from django.conf.urls import url
from . import views
from archiv import copy_views

app_name = 'archiv'
urlpatterns = [
    url(
        r'^hapabeleg-copy/$',
        copy_views.copy_beleg,
        name='copy_beleg'
    ),
    url(
        r'^hapabeleg/$',
        views.HapaBelegListView.as_view(),
        name='hapabeleg_browse'
    ),
    url(
        r'^hapabeleg/detail/(?P<pk>[0-9]+)$',
        views.HapaBelegDetailView.as_view(),
        name='hapabeleg_detail'
    ),
    url(
        r'^hapabeleg/create/$',
        views.HapaBelegCreate.as_view(),
        name='hapabeleg_create'
    ),
    url(
        r'^hapabeleg/edit/(?P<pk>[0-9]+)$',
        views.HapaBelegUpdate.as_view(),
        name='hapabeleg_edit'
    ),
    url(
        r'^hapabeleg/delete/(?P<pk>[0-9]+)$',
        views.HapaBelegDelete.as_view(),
        name='hapabeleg_delete'),
    url(
        r'^hapaplacename/$',
        views.HapaPlaceNameListView.as_view(),
        name='hapaplacename_browse'
    ),
    url(
        r'^hapaplacename/detail/(?P<pk>[0-9]+)$',
        views.HapaPlaceNameDetailView.as_view(),
        name='hapaplacename_detail'
    ),
    url(
        r'^hapaplacename/create/$',
        views.HapaPlaceNameCreate.as_view(),
        name='hapaplacename_create'
    ),
    url(
        r'^hapaplacename/edit/(?P<pk>[0-9]+)$',
        views.HapaPlaceNameUpdate.as_view(),
        name='hapaplacename_edit'
    ),
    url(
        r'^hapaplacename/delete/(?P<pk>[0-9]+)$',
        views.HapaPlaceNameDelete.as_view(),
        name='hapaplacename_delete'
    ),
    url(
        r'^hapamap/$',
        views.HapaMapDetailView.as_view(),
        name='hapamap_browser'
    ),
]
