from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

rooms = [
    {'id': 1, 'name': "Let's learn Python"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Frontend developpers"},
]

# Create your views here.
def home(request):
    context = {
        'rooms': Room.objects.all()
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    context = {
        'room': Room.objects.get(id=int(pk))
    }
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})