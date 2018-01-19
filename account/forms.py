from django import forms
from django.contrib.auth.models import User     # 引入django默认的用户模型User,
from .models import UserProfile


'''
forms.From: 通常用于提交表单，不对数据库进行修改
forms.ModelForm : 用于对数据库实现的操作，
'''
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput)
    class Meta:         # 声明本表单所应用的数据模型，
        model = User    # 告知写入User表内
        fields = ("username", "email",)

    def clean_password2(self):      # 检查用户输入的密码是否一致，  此方法在调用表单实例对象is_vaild时 会被执行
        # 以clean_+ 属性的名字，都有类似功能
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd["password2"]

class UserProfileFrom(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "brith")

