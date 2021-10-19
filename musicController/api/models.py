from django.db import models
import string  # for ascii chars
import random  # for random room code

"""""
Create models for db here.
Most of the logic should be in here, not in our views.
"""

"""
Every time a room is made, return a random and unique 6 digit code.
"""
def generate_unique_code():
    length = 6

    while True:
        # generate random code of length k with only uppercase ascii chars
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        
        # filter all Room objects to see if the code generated is a repeat
        number_of_repeats = Room.objects.filter(code=code).count()

        # if code generated is unique, stop generating
        if number_of_repeats == 0:
            break
    
    return code


class Room(models.Model):
    # unique code that identifies the room, uses generate_unique_code() defined above
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True) 

     # information stored that links back to our host
    host = models.CharField(max_length=50, unique=True)

    # permission to allow guest to pause music
    guest_can_pause = models.BooleanField(null=False, default=False)

    votes_to_skip = models.IntegerField(null=False, default=1)

    # when we create a new room, the date and time of creation is added automatically
    created_at = models.DateTimeField(auto_now_add=True)

