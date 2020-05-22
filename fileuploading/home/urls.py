from django.urls import  path
from .views import home,other
urlpatterns = [
    path('',home),
    path('other/', other, name = 'otherpage'),

]