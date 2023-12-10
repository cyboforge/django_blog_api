from rest_framework import serializers
from blog.models import Post
from user.serializers import UserMinSerializer


class PostSerializer(serializers.ModelSerializer):
  created_by = UserMinSerializer(read_only=True)

  class Meta:
    model = Post
    fields = '__all__'
    
  def create(self, validated_data):
    validated_data['created_by'] = self.context['request'].user
    return super().create(validated_data)