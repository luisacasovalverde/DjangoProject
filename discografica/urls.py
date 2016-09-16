from . import views
from django.conf import settings
from django.conf.urls import *
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<n>[0-9]+)$', views.loadPagina),
    url(r'^letra/(?P<id>[0-9]+)/$', views.letra, name='letra'),
    url(r'^album/(?P<id_album>[0-9]+)/$', views.album, name='album'),
    url(r'^form/album/$', views.form_album, name='form_album'),
    url(r'^form/artista/$', views.form_artista, name='form_artista'),
    url(r'^form/cancion/$', views.form_cancion, name='form_cancion'),
    url(r'^form/check/$', views.form_check, name='form_check'),
    url(r'^form/action/$', views.panel_action, name='form_action'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.login_user, name='login'),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),
]
