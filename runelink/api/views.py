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
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from OSRS_Hiscores import Hiscores
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


def get_ge_prices(request):
    url = "https://prices.runescape.wiki/api/v1/osrs/mapping"
    response = requests.get(url)
    data = response.json()
    sorted_data = sorted(data, key=lambda k: k["id"], reverse=False)
    page_num = request.GET.get("page", 1)

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
    searched_item = request.GET.get("item")
    api = osrs.OsrsPrices(identification="extreme4all#6456")
    items_id = items.getItemID(searched_item)
    data = api.itemDetail(item_id=items_id)
    print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    user_rsn = ""

    def post(self, request, format="json"):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                print(user.id)
                json = serializer.data
                user_rsn = json["rsn"]
                username = user_rsn
                username = username.replace(" ", "%20")
                user_call = Hiscores(username, "N")
                stats = user_call.stats
                print(stats)
                user_stats = SkillLevels(
                    user=user,
                    total= stats["total"]["level"],
                    attack=stats["attack"]["level"],
                    defense=stats["defense"]["level"],
                    strength=stats["strength"]["level"],
                    hitpoints=stats["hitpoints"]["level"],
                    ranged=stats["ranged"]["level"],
                    prayer=stats["prayer"]["level"],
                    magic=stats["magic"]["level"],
                    cooking=stats["cooking"]["level"],
                    woodcutting=stats["woodcutting"]["level"],
                    fletching=stats["fletching"]["level"],
                    fishing=stats["fishing"]["level"],
                    firemaking=stats["firemaking"]["level"],
                    crafting=stats["crafting"]["level"],
                    smithing=stats["smithing"]["level"],
                    mining=stats["mining"]["level"],
                    herblore=stats["herblore"]["level"],
                    agility=stats["agility"]["level"],
                    thieving=stats["thieving"]["level"],
                    slayer=stats["slayer"]["level"],
                    farming=stats["farming"]["level"],
                    runecrafting=stats["runecrafting"]["level"],
                    hunter=stats["hunter"]["level"],
                    construction=stats["construction"]["level"],
                )
                print(user_stats)
                user_stats.save()

                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GroupFinderViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = GroupFinder.objects.all().order_by('-time_posted')
    serializer_class = GroupFinderSerializer

    
class GroupFinderCommentsViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = GroupFinderComments.objects.all().order_by('-time_posted')
    serializer_class = GroupFinderCommentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    # def perform_create(self, serializer):
    #     serializer.save(post=self.request.post)
    
   

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


