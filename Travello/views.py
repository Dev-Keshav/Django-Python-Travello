from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'New Delhi'
    dest1.desc = 'The capital city of india'
    dest1.img = 'delhi.jpg'
    dest1.price = 500

    return render(request, 'index.html', {'dest1': dest1})
