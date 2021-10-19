from django.urls import path
from .views import index


urlpatterns = [

    
    # 1st argument refers to the route to be taken, specified in switch tags in App.js
    # 2nd argument index refers to index.js in src, which utilizes App.js
    

    # render the index template whenever we have a blank route
    path('', index),

    # render the join route
    path('join', index),

    # render the create route
    path('create', index),

    # added
    path('join/1', index)
]