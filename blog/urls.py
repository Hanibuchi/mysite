from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('list/', BlogList.as_view(), name='blog_list'),
    path('detail/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
]