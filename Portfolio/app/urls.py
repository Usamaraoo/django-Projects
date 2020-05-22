from django.urls import path, include, re_path
from .views import DeveloperDetail, NewDeveloper, success, DeveloperList

app_name = 'app'
urlpatterns = [
    path('', DeveloperList.as_view(), name='list'),
    path('<int:pk>', DeveloperDetail.as_view(), name='dev_detail'),
    path('c/', NewDeveloper.as_view(), name='newdev'),
    path('success/', success, name='success'),

]
