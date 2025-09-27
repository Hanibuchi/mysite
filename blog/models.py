from django.db import models
from django.conf import settings # ユーザーモデルを扱うために必要
import pykakasi

def japanese_to_romaji(text: str) -> str:
    kakasi = pykakasi.kakasi()

    # 直接 convert() を呼ぶ
    result = kakasi.convert(text)

    romaji = "-".join([item["hepburn"] for item in result])
    return romaji

class Tag(models.Model):
    """
    ブログ記事のタグを定義するモデル
    """
    name = models.CharField(max_length=50, unique=True, verbose_name="タグ名")
    slug = models.SlugField(unique=True, blank=True, verbose_name="スラッグ")

    def save(self, *args, **kwargs):
        """
        保存時に自動でスラッグを生成
        """
        if not self.slug:
            self.slug = japanese_to_romaji(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    ブログ記事を定義するモデル
    """
    title = models.CharField(max_length=200, verbose_name="タイトル")
    content = models.TextField(verbose_name="本文")
    thumbnail = models.ImageField(upload_to="post_thumbnails/", blank=True, null=True, verbose_name="サムネイル")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    slug = models.SlugField(unique=True, blank=True, verbose_name="スラッグ")
    
    # タグと記事を多対多で紐づける
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="タグ")

    def save(self, *args, **kwargs):
        """
        保存時に自動でスラッグを生成
        """
        if not self.slug:
            self.slug = japanese_to_romaji(self.title)
        super().save(*args, **kwargs)
    
    def total_likes(self):
        """
        記事のいいね総数を取得する
        (Likeモデルを参照しているため、ここではリレーション名はlike_setを使用)
        """
        # LikeモデルからこのPostに関連するLikeオブジェクトの数をカウント
        return self.like_set.count() # または self.likes.count() (related_nameによる)

    def __str__(self):
        return self.title

class Like(models.Model):
    """
    ユーザーのいいねを記録するモデル
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # デフォルトのリレーション名は post.like_set
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

    class Meta:
        # 一人のユーザーが一つの記事に複数いいねできないようにする制約
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'
