from django.urls import path
from .views import RoomView, CreateRoomView # so urls can use our views we made

urlpatterns = [
    # take Roomview class and give the view of the room when going to api/room
    # this is our api endpoint
    path('room', RoomView.as_view()),

    # if path is create-room, we can create a room with CreateRoomView class
    path('create-room', CreateRoomView.as_view())
]

