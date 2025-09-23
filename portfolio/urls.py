from django.urls import path
from .views import PortfolioList, PortfolioDetail

urlpatterns = [
    path('list/', PortfolioList.as_view(), name='portfolio_list'),
    path('detail/<slug:slug>/', PortfolioDetail.as_view(), name='portfolio_detail'),
]