from django.urls import path
from .views import BlogList, BlogDetail, TagBlogList

urlpatterns = [
    path('list/', BlogList.as_view(), name='blog_list'),
    path('detail/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('tag/<slug:tag_slug>/', TagBlogList.as_view(), name='tag_blog_list'),  # 追加
]