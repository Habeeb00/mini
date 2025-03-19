from .views import *
from django.urls import path

urlpatterns=[
    path('search/',search_item,name='search_items'), #Food search api no template backend
    path('searchpage/',search_page,name='search_page'), #Takes to search page
    path('selectserve/',select_serving,name='select_serving'), #Takes to food intake details entry
    path('save_meal/', save_meal, name='save_meal') #Daily food intake storing to db backend
]