# takes our model (room) and translates it into a JSON response

from rest_framework import serializers
from .models import Room


"""
Outgoing serializer to handle a response. 
Takes a room object, and serializes it into a possible response.
"""
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room

        # fields are same as the attributes in Room Class in models.py
        # id is unique integer that is made when room is created
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

"""
Incoming serializer to handle a post request. Ensures that the data
sent in the post request is valid and matches criteria for a new room.
Serializer object will be used to convert the post request data
(if valid) to data that Python can handle.
"""
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')