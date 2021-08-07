from django.urls import path
from . import views
#from . import show_poke_form
  
urlpatterns = [
   path('', views.index, name='index'),
   path('types/', views.types, name='types'),
   #path('type/',show_poke_form.show_poke_form, name='show_poke_view'),
  ]