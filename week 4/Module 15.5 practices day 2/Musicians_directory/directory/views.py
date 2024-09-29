from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm


# List all musicians and albums
def musician_list(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'directory/home.html', {'musicians': musicians, 'albums': albums})

# Create or edit musician
def musician_edit(request, id=None):
    musician = get_object_or_404(Musician, id=id) if id else None
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'directory/musician_form.html', {'form': form})

# Create or edit album
def album_edit(request, id=None):
    album = get_object_or_404(Album, id=id) if id else None
    musician_id = request.GET.get('musician_id', None)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
        if musician_id:  
            form.fields['musician'].initial = Musician.objects.get(id=musician_id)
    return render(request, 'directory/album_form.html', {'form': form})

# Delete musician
def musician_delete(request, id):
    musician = get_object_or_404(Musician, id=id)
    musician.delete()
    return redirect('musician_list')

# Delete album
def album_delete(request, id):
    album = get_object_or_404(Album, id=id)
    album.delete()
    return redirect('musician_list')