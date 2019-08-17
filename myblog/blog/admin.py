from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里显示想要显示的字段
    list_display = ['id', 'category', 'title', 'tui', 'user', 'views', 'created_time']
    # 满50条数据自动分页
    list_per_page = 50
    # 后台数据排序方式
    ordering = ['-created_time',]
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ['id', 'title']


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','linkurl')
