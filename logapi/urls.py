
from django.urls import path
from . import views

urlpatterns = [
  
  path('logdata/',views.ShowAll, name='logdata'),
  path('createlog/',views.CreateLog, name='createlog'),
  
]