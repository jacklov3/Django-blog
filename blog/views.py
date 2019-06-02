from django.shortcuts import render, get_object_or_404
import markdown
# Create your views here.
from django.http import HttpResponse
from .models import Post,Category
from comments.forms import CommentForm


# 返回渲染的博客主页
def index(request):
    # 从数据库中查询所有文章并按时间排序
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 返回渲染的文章详情主页
def detail(request, pk):
    # 查询是否有该文章
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ]
                                  )
    form =CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list,
    }

    return render(request, 'blog/detail.html', context=context)

#时间归档视图函数
def archives(request,year,month):
    #这里遇大坑，MYsql数据库时区的问题，google了才解决
    post_list = Post.objects.filter(created_time__year=year,created_time__month=month)
    print(post_list)
    return render(request,'blog/index.html',context={'post_list': post_list})

#分类页面
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list': post_list})


