from django.urls import reverse_lazy
# 既存機能である汎用ビューの CreateView をインポート
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm # 作成したフォームをインポート

class SignUpView(CreateView):
    # フォームに CustomUserCreationForm を使うことを指定
    form_class = CustomUserCreationForm
    
    # 使用するテンプレートファイルを指定
    template_name = 'registration/signup.html'
    
    # ユーザー作成成功後にリダイレクトするURLを指定
    success_url = reverse_lazy('login')

    # 注: CreateViewは is_valid() のチェック、form.save() の実行、
    # および成功時のリダイレクトを全て自動で行います。