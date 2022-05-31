from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from api.customviewset import CreateListViewSet
from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    PostSerializer,
    CommentSerializer,
    GroupsSerializer,
    FollowSerializer
)
from posts.models import Post, Group, User


class PostViewSet(viewsets.ModelViewSet):
    """View class for Post model."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ComentsViewSet(viewsets.ModelViewSet):
    """View class for Coment model."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        post = self.__get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.__get_post()
        serializer.save(author=self.request.user, post=post)

    def __get_post(self) -> Post:
        """Get post by id"""
        pk_post = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=pk_post)


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    """View class for Group model."""
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = (AllowAny, )


class FollowViewSet(CreateListViewSet):
    """View class for Follow model.
    Shows subscriptions and allows you to subscribe"""
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        follower = self.request.user
        return follower.following.all()

    def perform_create(self, serializer):
        following = get_object_or_404(
            User,
            username=self.request.data['following']
        )
        serializer.save(user=self.request.user, following=following)
