from django.db import models
from django.contrib.auth.models import User
# 导入Django自带的用户模块
from DjangoUeditor.models import UEditorField
# DjangoUeditor是基于python2.7的,对python3的支持有问题,所有我从网站找了支持python3的安装包

# Create your models here.


# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='博客分类')
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        db_table = 'category'
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签表
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='文章标签')

    class Meta:
        db_table = 'tag'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章推荐位表
class Tui(models.Model):
    name = models.CharField(max_length=100, verbose_name='推荐位')

    class Meta:
        db_table = 'tui'
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    excerpt = models.TextField(max_length=200, verbose_name='摘要', blank=True)
    # 使用外键关联分类表与分类是一对多关系
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联标签表与标签是多对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    # body = HTMLField()
    body = UEditorField('内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    # 文章作者，这里User是从django.contrib.auth.models导入的。这里我们通过ForeignKey把文章和User关联了起来。
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField('阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 轮播图
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    class Meta:
        db_table = 'banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info


# 友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址',max_length=100)

    class Meta:
        db_table = 'link'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
