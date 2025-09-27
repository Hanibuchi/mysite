from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Tag, Like
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
  
  # ユーザーが「いいね」しているかどうかの情報をコンテキストに追加
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post = self.get_object()
    is_liked = False
    
    # ユーザーがログインしている場合にのみLikeの状態を確認
    if self.request.user.is_authenticated:
      is_liked = post.like_set.filter(user=self.request.user).exists()
      
    context['is_liked'] = is_liked
    return context
  
@login_required # ログインしていないユーザーはログインページへリダイレクト
def like_post(request, slug):
  # POSTリクエストのみを処理
  if request.method == 'POST':
    post = get_object_or_404(Post, slug=slug)
    user = request.user
    
    # 既にいいねしているか確認
    like_instance = Like.objects.filter(post=post, user=user)
    
    if like_instance.exists():
      # 既にいいねしている場合は削除（いいね解除）
      like_instance.delete()
    else:
      # いいねしていない場合は作成（いいね）
      Like.objects.create(post=post, user=user)
      
    redirect_url = reverse('blog_detail', args=[slug]) + '#like-section' 
    return HttpResponseRedirect(redirect_url)
  return HttpResponseRedirect(reverse('blog_detail', args=[slug]) + '#like-section')