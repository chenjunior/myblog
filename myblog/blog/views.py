from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Banner, Tui, Tag, Article, Link

# Create your views here.


def index(request):
    # 查出所有的分类
    category = Category.objects.all()
    # 轮播图 查询所有的轮播图
    banner = Banner.objects.filter(is_active=True)
    # 首页推荐id为2 查询首页推荐的文章前三篇
    tui = Article.objects.filter(tui__id=2)[:3]
    # 最新文章 查询出全部文章,并用创建时间排序
    article = Article.objects.all().order_by('-created_time')[0:10]
    # 热门文章 查询以阅读量为排序方式
    hot = Article.objects.all().order_by('views')[0:10]
    # 热门推荐id为3,并截取前6个
    remen = Article.objects.filter(tui__id=3)[0:6]
    # 获取所有的标签
    tags = Tag.objects.all()
    # 获取友情链接表Link
    link = Link.objects.all()

    # print(banner)
    # print(category)
    context = {
        'category': category,
        'banner': banner,
        'tui': tui,
        'article': article,
        'hot': hot,
        'remen': remen,
        'tags': tags,
        'link': link,
        }

    return render(request, 'index.html', context)


def news(request):
    pass


def bbs(request):
    pass


def list(request):
    pass


def show(request):
    pass


def tags(request):
    pass


def search(request):
    pass


def about(request):
    pass

