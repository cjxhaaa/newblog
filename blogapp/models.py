from django.db import models

class Article(models.Model):
    title = models.CharField('标题',max_length = 40,default = 'title')
    content = models.TextField('正文',null = True)
    pub_time = models.DateTimeField('日期',null = True)
    def __str__(self):
        return self.title
