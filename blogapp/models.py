from django.db import models

class Category(models.Model):
    '''
    博客分类
    '''
    name = models.CharField('类名',max_length=20)

    def __str__(self):
        return self.name

class Tag(models.Model):
    '''
    博客标签
    '''
    name = models.CharField('名称',max_length=16)

    def __str__(self):
        return self.name

class Blog(models.Model):
    '''
    博客
    '''
    #CharField一个用来存储从小到很大各种长度的字符串的地方
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    #TextField大文本字段
    content = models.TextField('正文')
    # auto_now_add = True当对象第一次被创建时自动设置当前时间
    pub_time = models.DateTimeField('创建时间',auto_now_add=True)
    #auto_now=True每次保存对象时，自动设置该字段为当前时间
    change_time = models.DateTimeField('修改时间',auto_now=True)
    #ForeignKey多对一关系。需要一个位置参数：与该模型关联的类。
    # 若要创建一个递归的关联，对象与自己具有多对一的关系，请使用models.ForeignKey('self')。
    # 如果你需要关联到一个还没有定义的模型，你可以使用模型的名字而不用模型对象本身
    #verbose_name一个字段的可读性更高的名称
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.SET_NULL,null=True)
    #ManyToManyField一个多对多关联。要求一个关键字参数：与该模型关联的类，与ForeignKey 的工作方式完全一样
    tags = models.ManyToManyField(Tag,verbose_name='标签')

    class Meta:
        ordering = ['-pub_time']
    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    评论
    '''
    name = models.CharField('称呼',max_length=32)
    # EmailField检查输入的email地址是否合法
    # email = models.EmailField('邮箱')
    context = models.CharField('内容',max_length=300)
    pub_time = models.DateTimeField('评论时间',auto_now_add=True)
    blog = models.ForeignKey(Blog, verbose_name='评论所属文章', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-pub_time']

    def __str__(self):
        return self.context[:20]
