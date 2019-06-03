from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class AllPostsRssFeed(Feed):
    title = 'JackyLove\'s个人博客'
    link = '/'
    description = 'JackyLove的个人技术博客'

    #需要显示的内容
    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s'%(item.category,item.title)

    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return reverse('rss')