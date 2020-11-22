from django.urls import path
from .views import ImageViewList

urlpatterns = [
    path('Image/', ImageViewList, name='ImageAPIListView'),
]