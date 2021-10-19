from django.shortcuts import render

# Create your views here.

# render our index template and take care of it.
def index(request, *args, **kwargs):
    # takes request and index template and returns the html
    return render(request, 'frontend/index.html')