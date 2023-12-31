from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('albums/', views.AlbumList.as_view(), name="album_list"),
    path('albums/new/', views.AlbumCreate.as_view(), name="album_create"),
    path('albums/<int:pk>', views.AlbumDetail.as_view(), name="album_detail"),
    path('albums/<int:pk>/update', views.AlbumUpdate.as_view(), name="album_update"),
    path('albums/<int:pk>/delete', views.AlbumDelete.as_view(), name="album_delete"),
    path('albums/<int:pk>/songs/new', views.SongCreate.as_view(), name="song_create"),
    path('playlists/<int:pk>/songs/<int:song_pk>/', views.PlaylistSongAssoc.as_view(), name="playlist_song_assoc"),
    
]