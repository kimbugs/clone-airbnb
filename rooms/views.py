from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def see_all_rooms(request):
    rooms = Room.objects.all()
    content = {
        "rooms": rooms,
        "title": "title!!"
    }
    return render(request, "all_rooms.html", content)

def see_one_room(request, room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
        content = {
            "room": room
        }
        return render(request, "room_detail.html", content)
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True
            }
        )