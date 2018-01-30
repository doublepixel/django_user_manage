from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


'''
模型之间的关系为三种：  1、一对一  OneToOneField
                    2、一对多  ForeignKey
                    3、多对多  ManyToManyField
'''