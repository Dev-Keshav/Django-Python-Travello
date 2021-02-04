from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'New Delhi'
    dest1.desc = 'The capital city of india'
    dest1.img = 'delhi.jpg'
    dest1.price = 500

    dest2 = Destination()
    dest2.name = 'Mumbai'
    dest2.desc = 'The dream city of india'
    dest2.img = 'mumbai.jpg'
    dest2.price = 600

    dest3 = Destination()
    dest3.name = 'Goa'
    dest3.desc = 'Vacation destination of indians'
    dest3.img = 'goa.jpg'
    dest3.price = 700

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
