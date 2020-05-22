from django.urls import path, include
from app import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('dev', views.QuestionApi)

app_name = 'app'
urlpatterns = [
    path('', views.DevList.as_view(), name='list'),
    path('(?P<pk>\d+)', views.DevDetail.as_view(), name='detail'),
    path('api/', include(routers.urls), name='api'),

]
