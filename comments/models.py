from django.db import models

# Create your models here.


#Comment表
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    #外键，多对一的关系,删除时级联
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
