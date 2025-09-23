from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio
from django.urls import reverse_lazy
# Create your views here.

class PortfolioList(ListView):
  template_name = 'portfolio-list.html'
  model = Portfolio
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['active_page'] = 'portfolio-list'
    return context
  
class PortfolioDetail(DetailView):
  template_name = 'portfolio-detail.html'
  model = Portfolio