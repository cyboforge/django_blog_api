from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.apiviews import PostApiViewSet

router = DefaultRouter()
router.register(r'post', PostApiViewSet)


urlpatterns = [
  path('',include(router.urls)),
]