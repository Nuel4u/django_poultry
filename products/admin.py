from django.contrib import admin
from .models import LiveProducts,FrozonProducts ,BreedProducts

# Register your models here.

class liveAdmin(admin.ModelAdmin):
    list_display = ('name' ,'description','offer','price')


class frozenAdmin(admin.ModelAdmin):
    list_display =('name','offer','price')


class BreedAdmin(admin.ModelAdmin):
    list_display =('name' ,'offer','price')    

admin.site.register(LiveProducts ,liveAdmin)
admin.site.register(FrozonProducts ,frozenAdmin)
admin.site.register(BreedProducts ,BreedAdmin)