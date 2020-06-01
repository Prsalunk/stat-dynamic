from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'pune'
    dest1.price = 2000
    dest1.desc = 'Sooo many experiences'
    dest1.image = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name = 'mumbai'
    dest2.price = 1000
    dest2.desc = 'Cheap logonka residences'
    dest2.image = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name = 'hyderabad'
    dest3.price = 3000
    dest3.desc = 'Wanna go for Biryani'
    dest3.image = 'destination_3.jpg'

    dests = [dest1,dest2,dest3]

    return render(request, 'index.html', {'dests':dests})
