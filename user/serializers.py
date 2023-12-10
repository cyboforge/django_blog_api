
from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      'password': {
        'write_only':True
      }
    }
  def create(self, validated_data):
    password = validated_data.pop('password')
    user = super().create(validated_data)
    user.set_password(password)
    user.save()
    return user 
  
  def update(self, instance, validated_data):
    password = validated_data.pop('password', None)
    user = super().update(instance, validated_data)
    if password:
      user.set_password(password)
      user.save()
    return user



class UserMinSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'first_name', 'last_name']

class LogInSerializer(serializers.Serializer):
  email = serializers.EmailField(required=True)
  password = serializers.CharField(max_length=256, required=True)
