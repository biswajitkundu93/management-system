from django.urls import path, include 
from .views import *

urlpatterns = [
     path('auth/', include('app.auths.urls')),
     path('', index)
]