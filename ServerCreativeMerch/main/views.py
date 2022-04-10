from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *


class MerchAPIListPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page-size'
    max_page_size = 10000


class MerchAPIList(viewsets.ModelViewSet):
    queryset = Merch.objects.all()
    serializer_class = MerchSerialazer
    PageNumberPagination = MerchAPIListPagination


class UserAPIView(APIView):
    def get(self, request):
        user = Token.objects.get(key=request.GET.get('token')).user
        return Response(UserSerialazer(user).data)


class OrdersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerialazer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
