from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .models import BlogPost
from .pagination import BlogPostPagination
from .permissions import UpdateOwnBlog
from .serializers import (
    BlogPostListSerializer,
    BlogPostDetailSerializer,
)

#List of all Blog post
class BlogPostListAPIView(ListAPIView):
    queryset = BlogPost.objects.all().order_by('-id')
    serializer_class = BlogPostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__username', 'content']
    pagination_class = BlogPostPagination

#Blog post detail view
class BlogPostDetailAPIView(
        RetrieveAPIView,
        UpdateAPIView,
        DestroyAPIView,
    ):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        UpdateOwnBlog,
    )

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

#This view for create a new bog by auth user
class BlogPostCreateAPIView(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#Blog post Update view
"""class BlogPostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (
        IsAuthenticated,
        UpdateOwnBlog
    )

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)"""

#Blog post delete view
"""class BlogPostDeleteAPIView(DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer"""

