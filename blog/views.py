from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Tag
from django.urls import reverse_lazy
# Create your views here.

class BlogList(ListView):
  template_name = 'blog-list.html'
  model = Post
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['active_page'] = 'blog-list'
    return context

class TagBlogList(ListView):
  template_name = 'blog-list.html'
  
  def get_queryset(self):
    tag_slug = self.kwargs['tag_slug']
    tag = get_object_or_404(Tag, slug=tag_slug)
    return Post.objects.filter(tags=tag).order_by('-created_at')
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    tag_slug = self.kwargs['tag_slug']
    context['tag'] = get_object_or_404(Tag, slug=tag_slug)
    context['active_page'] = 'blog-list'
    return context
  
class BlogDetail(DetailView):
  template_name = 'blog-detail.html'
  model = Post