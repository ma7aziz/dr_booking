from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('details/<int:doctor_id>', views.details, name='details'),
    path('book/<int:doctor_id>',views.book, name='book')
    
]