from django.urls import path, include

from .views import (
   CommentCreateAPIView,
   CommentDetailAPIView,
   CommentListAPIView,
)



urlpatterns = [
   path('', CommentListAPIView.as_view(), name='list'),
   path('create/', CommentCreateAPIView.as_view(), name='create'),
   path('<int:pk>', CommentDetailAPIView.as_view(), name='thread'),
   #path('<int:pk>/update',BlogPostUpdateAPIView.as_view()),
   #path('<int:pk>/delete',BlogPostDeleteAPIView.as_view()),
]
