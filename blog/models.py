from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#分类表

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#文章表
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=100)
    # 文章摘要
    abstract = models.CharField(max_length=200, blank=True)
    #文章正文
    body = models.TextField()
    #文章作者,是多对一的关系，使用django给我们设计好的表
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #文章创建时间
    created_time = models.DateTimeField()
    #文章最新修改时间
    modified_time = models.DateTimeField()

    #外键关系：文章与分类是多对一的关系、所以在多的一端设置外键。
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #外键关系: 文章与标签是多对多的关系，一篇文章可以有多个标签，一个标签下可以有多篇文章。可以为空。多对多的关系定义在哪张表都可以
    #但是一般定义在需要编辑表单的地方，我们这里肯定是博客添加标签，而不是标签添加博客。
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']