from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from api.views import PostViewSet, ComentsViewSet, GroupsViewSet, FollowViewSet


post_router_v1 = SimpleRouter()
post_router_v1.register('posts', PostViewSet)
post_router_v1.register('groups', GroupsViewSet)
post_router_v1.register('follow', FollowViewSet, basename='follow')
post_router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    ComentsViewSet,
    basename='comment'
)

urlpatterns = [
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/', include(post_router_v1.urls)),
]
