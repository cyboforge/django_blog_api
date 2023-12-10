from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=255, blank=False, null=False)
  content = models.TextField(blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_by = models.ForeignKey('user.User', related_name='blog_post', on_delete=models.CASCADE, blank=False, null=False)

  def __str__(self):
    return self.title