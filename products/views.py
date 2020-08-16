from django.shortcuts import render,redirect
from .models import LiveProducts ,FrozonProducts ,BreedProducts
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def live(request):
    live = LiveProducts.objects.all()

    fros = FrozonProducts.objects.all()

    breed =  BreedProducts.objects.all()




    return render(request , 'ind.html' ,{'liveprod' : live ,'frozy':fros ,'breed': breed})
   # return render(request ,'products.html' ,{'frozy':fros})


def frozen(request ,id):
    fros = FrozonProducts.objects.filter(id = id)

    if int(id) ==1:

        return render(request , 'boneless.html',{'frozy':fros} )
    elif int(id) ==2:
        return render(request , 'breast.html',{'frozy':fros} )
         
    elif int(id) ==3:
        return render(request , 'drumstick.html',{'frozy':fros} )
        


    elif int(id) ==4:
        return render(request , 'chickenwings.html',{'frozy':fros} )

    elif int(id) ==5:
        return render(request , 'chickenbone.html',{'frozy':fros} )

    elif int(id) ==6:
        return render(request , 'tender.html',{'frozy':fros} )

    elif int(id) ==7:
        return render(request , 'legquarter.html',{'frozy':fros} )

    elif int(id) ==8:
        return render(request , 'whole.html',{'frozy':fros} )
    
    
    
 

    #return render(request ,'drumstick.html' ,{'frozy':fros})





def breading(request ,id):
    breed =  BreedProducts.objects.filter(id = id)

    return render(request ,'breed.html' ,{'breedproducts':breed})      

def index(request):
   return redirect('/') 


def product(request, id):

    livep = LiveProducts.objects.filter(id = id)
    
    #print("answer:" ,id)
    if int(id) ==1:

        return render(request , 'liveproducts.html',{'liveprod' : livep} )
    elif int(id) ==2:
        return render(request , 'goat.html',{'liveprod' : livep} )
         
    elif int(id) ==3:
        return render(request , 'fish.html',{'liveprod' : livep} )
        
   
    elif int(id) ==4:
        return render(request , 'egg.html',{'liveprod' : livep} )
   
    

    

def recipe(request, ad):
    # q = request.GET.get(id)q
    livep = LiveProducts.objects.filter(id = ad)
    return render(request, 'recipe.html', {'livegoods': livep})


def frozen_recipe(request , id):

    frozep = FrozonProducts.objects.filter(id = id)
    if int(id) == 1:
        return render(request, 'frozen_recipe.html', {'frozengoods': frozep })

    elif int(id) ==2:

        return render(request ,'skin_recipe.html' , {'frozengoods': frozep }) 

    elif int(id) ==3:

        return render(request ,'drum_recipe.html' , {'frozengoods': frozep }) 

    elif int(id) ==4:

        return render(request ,'wings_recipe.html' , {'frozengoods': frozep }) 

    elif int(id) ==5:

        return render(request ,'bone_recipe.html' , {'frozengoods': frozep }) 

    elif int(id) ==6:
        return render(request ,'tender_recipe.html' , {'frozengoods': frozep }) 
          
    elif int(id) ==7:

        return render(request ,'leg_recipe.html' , {'frozengoods': frozep }) 
      
    elif int(id) ==8:

        return render(request ,'whole_recipe.html' , {'frozengoods': frozep }) 
     

def breed_recipe(request ,id):
    breedp = BreedProducts.objects.filter(id = id)
    return render(request, 'breed_recipe.html', {'frozengoods': breedp })

def cook(request):
    return render(request ,'cooking.html')


def recipe_info(request):
    return render(request ,'recipe_info.html' )


def carrer(request):
    return render(request ,'carrer.html')    

def story(request):
    return render(request , 'story.html')    