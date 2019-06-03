from django.shortcuts import render, get_object_or_404
import markdown
# Create your views here.
from django.http import HttpResponse
from .models import Post,Category,Tag
from comments.forms import CommentForm
from django.views.generic import ListView,DetailView
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


#自定义获取全部列表通用视图类
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    #分页，每页10篇文章
    paginate_by = 10

#自定义获取分类列表的视图类，继承IndexView类
class CategoryView(IndexView):
    #重写获取的方法
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category=cate)

#自定义获取归档的视图类，依旧继承IndexView类
class ArchivesView(IndexView):
    #重写获取的方法
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        #这里注意mysql时区的设置
        return super(ArchivesView,self).get_queryset().filter(created_time__year=year,created_time__month=month)


#自定义标签的视图类
class TagView(IndexView):

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tags=tag)

#自定义获取详情的通用视图类
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    #重写get方法
    def get(self, request, *args, **kwargs):
        #先调用get方法，才会返回self.object属性
        response = super(PostDetailView,self).get(request,*args,**kwargs)
        #文章阅读量增加
        self.object.increase_views()
        return response

    #重写该方法，对post的body转化成HTML
    def get_object(self, queryset=None):
        post = super(PostDetailView,self).get_object(queryset=None)
        md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      TocExtension(slugify=slugify),
                                     ])


        post.conv_body = md.convert(post.body)
        post.toc = md.toc
        return post

    #重写get_context_data函数,添加评论的数据给模版文件
    def get_context_data(self, **kwargs):
        #这一步只获取到了post数据，详情页面还有评论的数据
        context = super(PostDetailView,self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context



#关于我页面
def about(request):
    return render(request,'blog/about.html')

#联系页面
def contact(request):
    return render(request,'blog/contact.html')




#
# # 返回渲染的博客主页
# def index(request):
#     # 从数据库中查询所有文章并按时间排序
#     post_list = Post.objects.all()
#     return render(request, 'blog/index.html', context={'post_list': post_list})
#
#
# # 返回渲染的文章详情主页
# def detail(request, pk):
#     # 查询是否有该文章
#     post = get_object_or_404(Post, pk=pk)
#     #增加阅读量
#     post.increase_views()
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       'markdown.extensions.toc',
#                                   ]
#                                   )
#     form =CommentForm()
#     comment_list = post.comment_set.all()
#     context = {
#         'post':post,
#         'form':form,
#         'comment_list':comment_list,
#     }
#
#     return render(request, 'blog/detail.html', context=context)
#
# #时间归档视图函数
# def archives(request,year,month):
#     #这里遇大坑，MYsql数据库时区的问题，google了才解决
#     post_list = Post.objects.filter(created_time__year=year,created_time__month=month)
#     return render(request,'blog/index.html',context={'post_list': post_list})
#
# #分类页面
# def category(request,pk):
#     cate = get_object_or_404(Category,pk=pk)
#     post_list = Post.objects.filter(category=cate)
#     return render(request,'blog/index.html',context={'post_list': post_list})


