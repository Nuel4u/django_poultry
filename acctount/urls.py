from django.urls import path
from .import views

urlpatterns =[
    path('register' ,views.register ,name='register'),
    path('login' , views.login , name='login'),
    path('logout' , views.logout , name='logout'),
    path('animate' ,views.animate ,name='animate'),
    path('heading' ,views.heading ,name='heading'),
    path('head' ,views.head ,name='head'),
    #path('recipe/' ,views.recipe ,name='recipe'),
]