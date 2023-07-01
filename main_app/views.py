from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Album, Song, Playlist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context


class About(TemplateView):
    template_name = "about.html"


class AlbumList(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["albums"] = Album.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context['albums'] = Album.objects.all()
            context["header"] = "Trending Albums"
        return context


class AlbumCreate(CreateView):
    model = Album
    fields = ['name', 'artist', 'image', 'info']
    template_name = "album_create.html"
    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.object.pk})


class AlbumDetail(DetailView):
    model = Album
    template_name = "album_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['name', 'artist', 'image', 'info']
    template_name = "album_update.html"
    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.object.pk})


class AlbumDelete(DeleteView):
    model = Album
    template_name = "album_delete.html"
    success_url = "/albums/"


class SongCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        album = Album.objects.get(pk=pk)
        Song.objects.create(title=title, length=length, album=album)
        return redirect('album_detail', pk=pk)


class PlaylistSongAssoc(View):
    def get(self, request, pk, song_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Playlist.objects.get(pk=pk).songs.remove(song_pk)
        if assoc == "add":
            Playlist.ojbects.get(pk=pk).songs.add(song_pk)
        return redirect('home')


