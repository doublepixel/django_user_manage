from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login  # 引入django内置的方法用户认证和用户管理
from .forms import LoginForm, RegistrationForm, UserProfileFrom
from django.contrib.auth.decorators import login_required
from .models import  UserInfo, UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect            # 实现URL的转化提交编辑表单之后，URL转化为my_information
from .forms import  UserProfileFrom, UserForm, UserInfoForm



# Create your views here.

# 创建登录视图函数user_login
def user_login(request):        # 视图函数必须使用 request作为第一个参数
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():           # 验证传入参数是否合法
            cd = login_form.cleaned_data        # 字典类型数据，以键值对的形式记录用户名和密码
            user = authenticate(username=cd['username'], password=cd['password'])
            # prin
            # print(user)
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


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileFrom(request.POST)
        print(userprofile_form)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)     # 仅生成数据对象，不保存至数据库中
            new_user.set_password(user_form.cleaned_data['password'])       # 设置该数据的对象密码
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, your can not register!")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileFrom()
        print(userprofile_form)
        return render(request, "account/register.html", {"form":user_form, "profile": userprofile_form})


@login_required(login_url='account/login')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)

    return render(request, "account/myself.html", {"user":user, "userinfo":userinfo, "userprofile":userprofile})

@login_required(login_url='account/login')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileFrom(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd["email"])
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd["profession"]
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()
        return  HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileFrom(initial={"birth":userprofile.birth,"phone":userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school":userinfo.school, "company":userinfo.company, "profession":userinfo.profession,
                                              "address":userinfo.address, "aboutme":userinfo.aboutme})
        return render(request, "account/myself_edit.html", {"user_form":user_form, "userprofile_form":userprofile_form, "userinfo":userinfo_form})