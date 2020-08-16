from django.urls import path
from .import views

urlpatterns = [
    path('live', views.live , name='live') ,
    path('frozen/<id>/' ,views.frozen ,name='frozen'),
    path('breeding/<id>' ,views.breading ,name='breeding'),
    path('index',views.index , name='index'),
    path('product/<id>/',views.product,name='product'),
    path('recipe/<ad>/',views.recipe,name='recipe'),
    path('frozen_recipe/<id>/' ,views.frozen_recipe ,name='frozen_recipe'),
    path('breed_recipe/<id>/' ,views.breed_recipe ,name='breed_recipe'),
    path('cook',views.cook ,name='cook'),
    path('recipe_info' ,views.recipe_info , name='recipe_info'),
    path('carrer' , views.carrer ,name='carrer'),
    path('story' ,views.story , name='story'),
  
    


]