from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    # url(r'^login/$', views.user_login, name="user_login"),        # 自定义登录
    url(r'^login/$', auth_views.login, name="user_login"),          # django内置方法登录
    url(r'^new_login/$', auth_views.login, {"template_name": "account/login.html"}),       # 传新的模板文件，需配置路径
    # url(r'^logout/$', auth_views.logout, name="user_logout"),  # 退出登录
    url(r'^logout/$', auth_views.logout,  {"template_name": "account/logout.html"}, name="user_logout"),  # 使用登录模板、退出登录
    url(r'^register/$', views.register, name="user_register"),  # 使用登录模板、退出登录
    url(r'^password-change/$', auth_views.password_change, {"post_change_redirect":"/account/password-change-done"}, name="password_change"),
    url(r'^password-change-done/$', auth_views.password_change_done, name="password_change_done"),

]