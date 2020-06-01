from django.db import models

# Create your models here.

class Destination:

    id = int
    name = str
    price = int
    desc = str
    image = str
    offr = bool