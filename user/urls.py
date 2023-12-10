from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.apiviews import Authentication, UserApiViewSet

router = DefaultRouter()
router.register(r'', UserApiViewSet)
router.register(r'authentication', Authentication, basename = 'authentication')


urlpatterns = [
  path('',include(router.urls)),
]
 