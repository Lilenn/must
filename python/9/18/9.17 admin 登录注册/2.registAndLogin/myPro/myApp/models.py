from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.backends import ModelBackend
# Create your models here.
import datetime
# 模型内容一旦发生改变  要重新迁移
class UserProfile(AbstractUser):
    unickname = models.CharField(max_length=20,verbose_name='昵称',null=True,blank=True)
    ubirthday = models.DateField(auto_now_add=True,verbose_name='生日',null=True,blank=True)
    uaddress = models.CharField(max_length=200,verbose_name='地址',null=True,blank=True)


class EmailRecord(models.Model):
    code = models.CharField( max_length=20)
    send_date = models.DateTimeField(default=datetime.datetime.now() )
    email = models.EmailField( error_messages={'invalid': '邮箱格式不正确'})

class ResetWithEmail(models.Model):
    email = models.EmailField(error_messages={'invalid':'重置邮箱错误'})

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(email=username)
            if user.check_password(password):
                return user
        except:
            return None



