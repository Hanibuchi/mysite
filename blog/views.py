from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class BlogList(ListView):
  template_name = 'blog-list.html'
  model = Post
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['active_page'] = 'blog-list'
    return context
  
class BlogDetail(DetailView):
  template_name = 'blog-detail.html'
  model = Post