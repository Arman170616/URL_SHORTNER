from django.urls import path
from .views import createUrl, routeToURL

urlpatterns = [
    path('', createUrl), 
    path('<slug:key>', routeToURL)
]