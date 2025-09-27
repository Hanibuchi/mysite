from django.shortcuts import render
from blog.models import Post
from portfolio.models import Portfolio

def main(request):
  latest_blogs = Post.objects.order_by('-updated_at')[:6]

  latest_portfolios = Portfolio.objects.order_by('-created_at')[:4]
  
  context = {
    'latest_blogs': latest_blogs,
    'latest_portfolios': latest_portfolios,
    'active_page': 'main',
  }
  
  return render(request, 'homepage.html', context)

def test(request):
  return render(request, 'login.html')