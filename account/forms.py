from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=False,
        label="メールアドレス",
        widget=forms.EmailInput(attrs={'placeholder': 'メールアドレスを入力してください'})
    )
    
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "password1", "password2") 
        
        labels = {
            "username": "ユーザー名",
            "password1": "パスワード",
            "password2": "パスワード（確認用）",
        }