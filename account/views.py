from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login  # 引入django内置的方法用户认证和用户管理
from .forms import LoginForm
# Create your views here.

# 创建登录视图函数user_login
def user_login(request):        # 视图函数必须使用 request作为第一个参数
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():           # 验证传入参数是否合法
            cd = login_form.cleaned_data        # 字典类型数据，以键值对的形式记录用户名和密码
            user = authenticate(username=cd['username'], password=cd['password'])
            # prin
            print(user)
            if user:
                login(request, user)
                return HttpResponse("welcome You. You have been authenticated successfully.")
            else:
                # print(cd)
                return HttpResponse("sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form":login_form})
