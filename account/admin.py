from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "school", "company", "profession", "address", "aboutme", "photo")
    list_filter = ("school", "company", "profession")

admin.site.register(UserInfo, UserInfoAdmin)