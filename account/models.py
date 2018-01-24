from django.db import models
from django.contrib.auth.models import User   #内置的用户管理应用数据模型

# Create your models here.
class UserProfile(models.Model):        # 对应着要在数据库中创建 userprofile 数据表,最终表名为：account_userprofile
    user = models.OneToOneField(User, unique=True)      # user表与当前user字段一一对应，如需要增加主键 primary_key=True
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    '''
    CharField: 用于保存字符串
    TextField : 保存字符串，无长度限制
    EmailField、URLField 继承了CharField
    DateField、DateTimeField:用于保存时间，格式为：1992-01-23
    '''

    def __str__(self):
        return 'user:{}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    """
    blank=True  表示可以为空
    """

    def __str__(self):
        return "user:{}".format(self.user.username)
