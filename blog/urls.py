from django.urls import path

from . import views

#添加命名空间，为多应用做预留，防止多应用中的URL混淆
app_name='blog'

urlpatterns=[
    #主页
    path('',views.index,name='index'),
    path('post/',views.index,name='index'),
    #文章详情页
    path('post/<int:pk>/',views.detail,name='detail'),
    #归档页
    path('archives/<int:year>/<int:month>',views.archives,name='archives'),
    #分类页
    path('category/<int:pk>',views.category,name='category'),

]