from django.test import TestCase
from django.core.exceptions import ValidationError
from blog.models import Post
from .models import Portfolio

class PortfolioModelTest(TestCase):
    """
    Portfolioモデルのテストクラス
    """
    def setUp(self):
        """
        各テストメソッドの実行前に呼び出される
        """
        # テスト用のブログ記事を作成
        self.post_title = "私の初めてのDjangoプロジェクト"
        self.blog_post = Post.objects.create(
            title=self.post_title,
            content="これはテスト記事です。"
        )

        # テスト用のポートフォリオ作品を作成
        self.portfolio_title = "テストポートフォリオ"
        self.portfolio = Portfolio.objects.create(
            title=self.portfolio_title,
            description="これはテストの概要です。",
            detailed_description="これは詳細な説明です。",
            live_site_url="https://example.com"
        )
    
    def test_portfolio_creation_and_slug(self):
        """
        作品が正しく作成され、スラッグが自動生成されるかテスト
        """
        # モデルのインスタンスが作成されたか確認
        self.assertEqual(Portfolio.objects.count(), 1)
        # スラッグが正しく自動生成されたか確認
        self.assertEqual(self.portfolio.slug, "tesutopootoforio")

    def test_related_blog_post(self):
        """
        関連ブログ記事が正しく紐づけられるかテスト
        """
        # ポートフォリオ作品にブログ記事を紐づけ
        self.portfolio.blog_post = self.blog_post
        self.portfolio.save()
        
        # 紐づけが正しいか確認
        self.assertEqual(self.portfolio.blog_post.title, self.post_title)

    def test_invalid_url_field(self):
        """
        無効なURLが入力された場合にValidationErrorが発生するかテスト
        """
        invalid_url = "not-a-valid-url"
        
        # モデルに無効なURLを設定
        self.portfolio.live_site_url = invalid_url
        
        # save()メソッドがValidationErrorを発生させるかテスト
        with self.assertRaises(ValidationError):
            self.portfolio.full_clean()
