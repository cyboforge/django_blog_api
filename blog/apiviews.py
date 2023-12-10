from rest_framework import viewsets
from blog.serializers import PostSerializer
from custom_permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .models import Post

class PostApiViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsOwnerOrReadOnly]