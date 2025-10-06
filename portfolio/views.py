from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Portfolio, TechStack
from django.urls import reverse_lazy
# Create your views here.

class PortfolioList(ListView):
  template_name = 'portfolio-list.html'
  model = Portfolio
  
  def get_queryset(self):
    """
    URLの tech_slug パラメータに基づいてフィルタリングを行う
    """
    queryset = super().get_queryset()
    
    # URLから技術スタックのスラッグを取得
    tech_slug = self.kwargs.get('tech_slug') 
    
    if tech_slug:
      # フィルタリング用のTechStackオブジェクトを取得
      # スラッグが見つからない場合は404を返す (TagBlogListのget_querysetと同様の処理)
      self.current_tech = get_object_or_404(TechStack, slug=tech_slug)
      
      # 取得したTechStackに関連付けられたPortfolioをフィルタリング
      queryset = queryset.filter(technologies=self.current_tech)
        
    return queryset.order_by('-created_at') # 作成日時の降順でソート
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    
    # get_querysetでTechStackオブジェクトを取得・設定していることを想定
    if hasattr(self, 'current_tech'):
      context['tech'] = self.current_tech

    context['active_page'] = 'portfolio-list'
    context['techstacks'] = TechStack.objects.all()
    return context
  
class PortfolioDetail(DetailView):
  template_name = 'portfolio-detail.html'
  model = Portfolio