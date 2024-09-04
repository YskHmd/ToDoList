from django.db import models

# Create your models here.

#タイトルと内容のクラス
class TodoModel(models.Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField()
    
    def __str__(self):
        return self.title
    
