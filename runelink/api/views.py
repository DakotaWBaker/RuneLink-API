from django.shortcuts import render
import requests
import json
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import pagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, ChildSerializer, ParentSerializer, TagSerializer
from .models import CustomUser, Parent, Child, Tag
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.


def get_ge_prices(request):
    url = "https://prices.runescape.wiki/api/v1/osrs/mapping"
    response = requests.get(url)
    data = response.json()
    sorted_data = sorted(data, key=lambda k: k['id'], reverse=False)
    page_num = request.GET.get('page', 1)

    paginator = Paginator(sorted_data, 25) 


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    result_list = list(page_obj)
    return HttpResponse(json.dumps(result_list), content_type="application/json")

def ge_search(request):
    from osrs import osrs
    from OSRSBytes import Items
    items = Items()
    searched_item = request.GET.get('item') 
    api = osrs.OsrsPrices(identification='extreme4all#6456')
    items_id = items.getItemID(searched_item)
    data = api.itemDetail(item_id=items_id)
    return HttpResponse(json.dumps(data), content_type="application/json")

 

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ChildViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ParentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer   