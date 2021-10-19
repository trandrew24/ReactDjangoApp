from django.shortcuts import render
from rest_framework import generics # allows us to create a class inheriting from generic api view
from rest_framework import status # Give us access to HTTP status codes that will be used when we return a custom response
from .serializers import RoomSerializer, CreateRoomSerializer # import serializer classes we made
from .models import Room # import Room class
from rest_framework.views import APIView # generic API view
from rest_framework.response import Response # allows for a custom response from our user to be returned

# Create your views here.
"""
API view that will let us view a list of the different rooms
as well as create a room.
Class inherits from generics in rest_framework
"""
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

"""
CreateRoomView inherits from APIView to allow us to override some default methods.
"""
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    # takes data from a post prequest and converts it to python data if valid
    def post(self, request, format=None):

        # check if the current user doesn't have an active session on our web server
        if not self.request.session.exists(self.request.session.session_key):
            # create a session
            self.request.session.create()

        # take our data from the post request and serialize it into python representation using CreateRoomSerializer
        serializer = self.serializer_class(data=request.data)
        # check the class serialized object is valid
        if serializer.is_valid():

            # initialize variables that represent the data we are taking from the request
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')

            # get the host's session key
            host = self.request.session.session_key

            # Here we check for if there is any room in the database that have the same host
            # This is the case if the host already has a room in their current session
            queryset = Room.objects.filter(host=host)

            # if the host already has a room, don't make a new room. Instead,
            # modify the current room's attributes to be what was sent in the post request.
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip

                # saves and only updates the fields for pause and skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])

                # custom response the user requested that contains the updated, serialized room
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)

            # Case where the host doesn't already have a room. We make a new room.
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save()

                # custom response the user requested that contains the newly created, serialized room
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        # post request from user was invalid return Bad Request Response
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


