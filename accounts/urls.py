from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()

router.register('signup',views.UserAccountsViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view()),
]