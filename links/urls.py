from django.urls import path
from .views import item_redirect_view

urlpatterns = [
    path('item_detail/<int:item_id>/', item_redirect_view, name='item_detail'),
]