from django.shortcuts import render 
from .models import Destination

# Create your views here.

def index(request):
    des = Destination.objects.all()
   # des = Destination()
    #des.name ='Toloto'
    #des.desc = 'Health and affordable'
    #des.img = 'bg-img/to1.jpeg'
    #des.offer =False

    #des2 = Destination()
    #des2.name ='Chicken'
    #des2.desc = 'Cheap Price'
    #des2.img = 'bg-img/ch2.jpeg'
    #des2.offer = False

    #des3 = Destination()
    #des3.name ='Hen'
    #des3.desc = 'Easy to cook'
    #des3.img = 'bg-img/go3.jpeg'
    #des3.offer = True

    #des4 = Destination()
    #des4.name ='Egg'
    #des4.desc = 'Easy to cook'
    #des4.img = 'bg-img/eg3.jpeg'
    #des4.offer = True

    #des6 = Destination()
    #des6.name ='Chicken'
    #des6.desc = 'Easy to cook'
    #des6.img = 'bg-img/fish1.jpg'
    #des6.offer = False

    #des5 = Destination()
    #des5.name ='Fish'
    #des5.desc = 'Delicious Fish'
    #des5.img = 'bg-img/fi1.jpg'
    #des5.offer = True

    #desti = [des ,des2 ,des3 ,des4 , des5,des6]

    return render(request , 'head.html' ,{"desty": des})
    
