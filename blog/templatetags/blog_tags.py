# 自定义模版标签

from blog.models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count
register = template.Library()

#自定义获取最新5篇文章的标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#自定义归档标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

#自定义归档标签
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

#自定义标签集合
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts= Count('post')).filter(num_posts__gt=0)
