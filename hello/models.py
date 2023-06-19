from django.db import models

# Create your models here.
from django.utils import timezone


class FileModel(models.Model):
    # 文件名称
    name = models.CharField(max_length=50)

    # 文件保存路径
    path = models.CharField(max_length=100)

    # 上传时间
    upload_time = models.DateTimeField(default=timezone.now)