from django.urls import path
from .views import *


urlpatterns = [
    path('api/catalog/', MerchAPIList.as_view({'get': 'list'})),
    path('api/catalog/<int:pk>', MerchAPIList.as_view({'get': 'retrieve'})),
    path('api/orders/', OrdersListCreateAPIView.as_view()),
    path('api/orders/<int:pk>', OrdersListCreateAPIView.as_view()),
    path('api/user', UserAPIView.as_view()),
]