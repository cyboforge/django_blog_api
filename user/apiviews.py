from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from custom_permissions import IsOwnerOrReadOnly
from user.models import User
from user.serializers import LogInSerializer, UserSerializer
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


class UserApiViewSet(viewsets.ModelViewSet):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsOwnerOrReadOnly]

  queryset = User.objects.all()
  serializer_class = UserSerializer

class Authentication(viewsets.ViewSet):

  @action(detail=False, methods=['POST'])
  def get_auth_token(self, request):
    serializer = LogInSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user_by_email = User.objects.filter(email=email).first()
        username = user_by_email.username if user_by_email else None
        user = authenticate(request, username=username, password=password)
        if user:
          token, created = Token.objects.get_or_create(user=user)
          return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
          return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)