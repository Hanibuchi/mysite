from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from .models import Tag, Post, Like

# ユーザーモデルを取得
User = get_user_model()

class TagModelTest(TestCase):
    """
    Tagモデルのテストケース
    """
    def test_tag_creation_and_slug(self):
        """
        タグが正しく作成され、スラッグが自動生成されるかテスト
        """
        tag_name = "Python開発"
        tag = Tag.objects.create(name=tag_name)
        self.assertEqual(tag.name, tag_name)
        self.assertEqual(tag.slug, "Python-kaihatsu")
    
    def test_tag_str_representation(self):
        """
        __str__メソッドが正しく動作するかテスト
        """
        tag = Tag.objects.create(name="Django")
        self.assertEqual(str(tag), "Django")

class PostModelTest(TestCase):
    """
    Postモデルのテストケース
    """
    def setUp(self):
        """
        テスト実行前のセットアップ
        """
        self.post_title = "私の初めてのブログ記事"
        self.post = Post.objects.create(title=self.post_title, content="これはテスト記事です。")

    def test_post_creation_and_slug(self):
        """
        記事が正しく作成され、スラッグが自動生成されるかテスト
        """
        self.assertEqual(self.post.title, self.post_title)
        self.assertEqual(self.post.slug, "watashi-no-hajimete-no-burogu-kiji")
    
    def test_post_str_representation(self):
        """
        __str__メソッドが正しく動作するかテスト
        """
        self.assertEqual(str(self.post), self.post_title)
        
    def test_post_with_tags(self):
        """
        記事にタグが正しく紐づけられるかテスト
        """
        tag1 = Tag.objects.create(name="プログラミング")
        tag2 = Tag.objects.create(name="Django")
        self.post.tags.add(tag1, tag2)
        self.assertEqual(self.post.tags.count(), 2)
        self.assertIn(tag1, self.post.tags.all())
        self.assertIn(tag2, self.post.tags.all())

class LikeModelTest(TestCase):
    """
    Likeモデルのテストケース
    """
    def setUp(self):
        """
        テスト実行前のセットアップ
        """
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.post = Post.objects.create(title="テスト記事", content="いいねのテストです。")

    def test_total_likes_method(self):
        """
        total_likesメソッドが正しくいいね数を返すかテスト
        """
        self.assertEqual(self.post.total_likes(), 0)
        Like.objects.create(user=self.user, post=self.post)
        self.assertEqual(self.post.total_likes(), 1)
    
    def test_unique_together_constraint(self):
        """
        同じユーザーが同じ記事に複数いいねできないかテスト
        """
        Like.objects.create(user=self.user, post=self.post)
        with self.assertRaises(IntegrityError):
            Like.objects.create(user=self.user, post=self.post)
            
    def test_related_name_access(self):
        """
        Postからrelated_nameでLikeオブジェクトにアクセスできるかテスト
        """
        Like.objects.create(user=self.user, post=self.post)
        self.assertEqual(self.post.likes.count(), 1)
        self.assertEqual(self.post.likes.first().user, self.user)
