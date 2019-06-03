from django.urls import path

from . import views

#添加命名空间，为多应用做预留，防止多应用中的URL混淆
app_name='blog'

urlpatterns=[
    #主页
    path('',views.IndexView.as_view(),name='index'),
    path('post/',views.IndexView.as_view(),name='index2'),
    #文章详情页
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    #归档页
    path('archives/<int:year>/<int:month>',views.ArchivesView.as_view(),name='archives'),
    #分类页
    path('category/<int:pk>',views.CategoryView.as_view(),name='category'),
    #标签页
    path('tag/<int:pk>',views.TagView.as_view(),name='tag'),
    #关于我
    path('about/',views.about,name='about'),
    #联系
    path('contact/', views.contact, name='contact'),


]