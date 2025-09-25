from django.contrib import admin
from .models import Portfolio, PortfolioImage, TechStack

admin.site.register(Portfolio)
admin.site.register(TechStack)

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'image', 'caption')