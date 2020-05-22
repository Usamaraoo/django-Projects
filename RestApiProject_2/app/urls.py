from django.urls import path, include
from app.views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Book', BookViewSet)
urlpatterns = [
    path('',include(router.urls))
]
