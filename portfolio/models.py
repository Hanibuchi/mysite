from django.db import models
from blog.models import Post
import pykakasi

def japanese_to_romaji(text: str) -> str:
    kakasi = pykakasi.kakasi()

    # 直接 convert() を呼ぶ
    result = kakasi.convert(text)

    romaji = "-".join([item["hepburn"] for item in result])
    return romaji

class TechStack(models.Model):
    """
    ポートフォリオに使用された技術スタックを管理するモデル
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="技術名")
    # スラッグフィールドを追加
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="スラッグ") 

    def __str__(self):
        return self.name
        
    # saveメソッドでスラッグを自動生成
    def save(self, *args, **kwargs):
        # スラッグが設定されていない場合、名前から自動生成する
        if not self.slug:
            self.slug = japanese_to_romaji(self.name)
        super().save(*args, **kwargs)

class Portfolio(models.Model):
    """
    ポートフォリオ作品のデータを管理するモデル
    """
    title = models.CharField(max_length=200, verbose_name="作品名")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="スラッグ")
    description = models.TextField(verbose_name="概要")
    detailed_description = models.TextField(blank=True, verbose_name="詳細説明")
    video_url = models.URLField(max_length=200, blank=True, verbose_name="紹介動画URL")
    live_site_url = models.URLField(max_length=200, blank=True, verbose_name="公開先URL")
    
    technologies = models.ManyToManyField(
        TechStack, 
        blank=True, 
        related_name='portfolios', 
        verbose_name="技術スタック"
    )
    
    # 関連するブログ記事へのForeignKey
    blog_post = models.ForeignKey(
        Post, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='portfolios',
        verbose_name="関連ブログ記事"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # スラッグが設定されていない場合、タイトルから自動生成する
        if not self.slug:
            self.slug = japanese_to_romaji(self.title)
        super().save(*args, **kwargs)

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.portfolio.title}"