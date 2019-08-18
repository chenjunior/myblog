from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 导入django自带的分页工具

from .models import Category, Banner, Tui, Tag, Article, Link

# Create your views here.


# 首页
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


# 列表页
def list(request, lid):
    print('*'*100)
    # lid代表的是当前文章的id
    # 获取对应的文章
    article = Article.objects.filter(category_id=lid).order_by('-created_time')
    # 获取当前文章的分类名字
    c_name = Category.objects.get(id=lid)
    print(c_name)
    # 获取右侧热门推荐
    remen = Article.objects.filter(tui__id=2)[0:6]
    # 获取所有的分类
    category = Category.objects.all()
    tags = Tag.objects.all()

    # 在url中获取当前分页的页数
    page = request.GET.get('page')
    # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    paginator = Paginator(article, 5)
    link = Link.objects.all()
    # print(link)
    try:
        # 获取当前页码的记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户输入的页码不是整数时,显示第1页的内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        list = paginator.page(paginator.num_pages)

    context = {
        'article': article,
        'c_name': c_name,
        'remen': remen,
        'category': category,
        'tags': tags,
        'list': list,
        'link': link
    }
    # print(context)

    return render(request, 'list.html', context)


# 详情页
def show(request, sid):
    article = Article.objects.get(id=sid)
    category = Category.objects.all()
    tags = Tag.objects.all()
    # 热门推荐id为3,并截取前6个
    remen = Article.objects.filter(tui__id=3)[0:6]
    # 内容下面的您可能感兴趣的文章，随机推荐
    hot = Article.objects.all().order_by('?')[0:10]
    # 上一篇文章,文章创建时间小的就是上一篇
    previous_blog = Article.objects.filter(
        created_time__gt=article.created_time,
        category=article.category.id
    ).first()
    # 下一篇文章,文章创建时间小的就是下一篇
    next_blog = Article.objects.filter(
        created_time__lt=article.created_time,
        category=article.category.id
    ).last()
    article.views = article.views + 1
    article.save()
    context = {
        'article': article,
        'category': category,
        'tags': tags,
        'remen': remen,
        'hot': hot,
        'previous_blog': previous_blog,
        'next_blog': next_blog,
    }

    return render(request, 'show.html', context)


def tags(request):
    pass


def search(request):
    pass


def about(request):
    print('*' * 100)
    pass

