from django.urls import path, include

from .views import (
   BlogPostListAPIView,
   BlogPostDetailAPIView,
   #BlogPostDeleteAPIView,
   #BlogPostUpdateAPIView,
   BlogPostCreateAPIView,
)



urlpatterns = [
   path('',BlogPostListAPIView.as_view()),
   path('create/',BlogPostCreateAPIView.as_view()),
   path('<int:pk>',BlogPostDetailAPIView.as_view(), name = 'detailAPI'),
   #path('<int:pk>/update',BlogPostUpdateAPIView.as_view()),
   #path('<int:pk>/delete',BlogPostDeleteAPIView.as_view()),
]
