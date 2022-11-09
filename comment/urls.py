from django.urls import path, include
from .views import home, geenerate_data #, search_elastic
# from .documents import CarDocument

urlpatterns = [
    path('', home, name='home'),
    path('generate', geenerate_data, name='generate'),
    # path('search/', search_elastic, name='search'),
]
