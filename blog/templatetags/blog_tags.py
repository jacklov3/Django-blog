# 自定义模版标签

from blog.models import Post,Category
from django import template
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
    return Category.objects.all()