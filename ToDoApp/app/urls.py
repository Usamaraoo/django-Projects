from django.urls import path
from app.views import app,delete,add_todo

urlpatterns = [
    path('', app),
    path('add_todo/', add_todo),
    path('delet_item/<int:item_id>/', delete),
]
