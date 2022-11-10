from django.urls import path, include
from .views import home, geenerate_data , search_elastic
# from .documents import CarDocument

urlpatterns = [
    path('', home, name='home'),
    # generating 500 comments 
    path('generate', geenerate_data, name='generate'),
    # elastic search page 
    path('search/', search_elastic, name='search'),
]
