from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'groupfinder', GroupFinderViewSet)
router.register(r'comment', GroupFinderCommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/',  UserDetail.as_view(), name="get_user_details"),
    path("grandexchange", views.get_ge_prices, name="restaurant data json"),
    path("gesearch", views.ge_search),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
