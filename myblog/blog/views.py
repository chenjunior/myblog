from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 导入django自带的分页工具

from .models import Category, Banner, Tag, Article, Link

# Create your views here.


# 优化
def global_variable(request):
    """下面的三个方法都是所有请求有用到的"""
    # 查出所有的分类
    category = Category.objects.all()
    # 热门推荐id为3,并截取前6个
    remen = Article.objects.filter(tui__id=3)[0:6]
    # 获取所有的标签
    tags = Tag.objects.all()

    return locals()


# 首页
def index(request):
    # 查出所有的分类
    # category = Category.objects.all()
    # 轮播图 查询所有的轮播图
    banner = Banner.objects.filter(is_active=True)
    # 首页推荐id为2 查询首页推荐的文章前三篇
    tui = Article.objects.filter(tui__id=2)[:3]
    # 最新文章 查询出全部文章,并用创建时间排序
    article = Article.objects.all().order_by('-created_time')[0:10]
    # 热门文章 查询以阅读量为排序方式
    hot = Article.objects.all().order_by('views')[0:10]
    # 热门推荐id为3,并截取前6个
    # remen = Article.objects.filter(tui__id=3)[0:6]
    # 获取所有的标签
    # tags = Tag.objects.all()
    # 获取友情链接表Link
    link = Link.objects.all()

    # print(banner)
    # print(category)
    # context = {
    #     'category': category,
    #     'banner': banner,
    #     'tui': tui,
    #     'article': article,
    #     'hot': hot,
    #     'remen': remen,
    #     'tags': tags,
    #     'link': link,
    #     }

    return render(request, 'index.html', locals())


# 列表页
def list(request, lid):
    # print('*' * 100)
    # lid代表的是当前文章的id
    # 获取对应的文章
    article = Article.objects.filter(category_id=lid).order_by('-created_time')
    # 获取当前文章的分类名字
    c_name = Category.objects.get(id=lid)
    print(c_name)
    # 获取右侧热门推荐
    # remen = Article.objects.filter(tui__id=2)[0:6]
    # 获取所有的分类
    # category = Category.objects.all()
    # tags = Tag.objects.all()

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

    # context = {
    #     'article': article,
    #     'c_name': c_name,
    #     'remen': remen,
    #     'category': category,
    #     'tags': tags,
    #     'list': list,
    #     'link': link
    # }
    # print(context)

    return render(request, 'list.html', locals())


# 详情页
def show(request, sid):
    article = Article.objects.get(id=sid)
    # category = Category.objects.all()
    # tags = Tag.objects.all()
    # 热门推荐id为3,并截取前6个
    # remen = Article.objects.filter(tui__id=3)[0:6]
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
    # context = {
    #     'article': article,
    #     'category': category,
    #     'tags': tags,
    #     'remen': remen,
    #     'hot': hot,
    #     'previous_blog': previous_blog,
    #     'next_blog': next_blog,
    # }

    return render(request, 'show.html', locals())


def tags(request, tag):
    # print('*' * 100)
    # 获取标签为tag的所有文章
    article = Article.objects.filter(tags__name=tag)
    # 获取右侧热门推荐
    # remen = Article.objects.filter(tui__id=3)[0:6]
    # 获取所有的分类
    # category = Category.objects.all()
    # 获取当前搜索的标签
    t_name = Tag.objects.get(name=tag)
    # tags = Tag.objects.all()
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

    # context = {
    #     'article': article,
    #     't_name': t_name,
    #     'remen': remen,
    #     'category': category,
    #     'tags': tags,
    #     'list': list,
    #     'link': link
    # }
    # print(context)

    return render(request, 'tags.html', locals())


def search(request):
    # 获取前端提交搜索的名字
    ss = request.GET.get('search')
    print('*'*100)
    print(ss)
    # 获取标题为ss的文章,title__icontains是用ss和文章标题进行匹配,
    # 如果标题包含ss,就会被筛选出来,__icontains部不分大小写
    article = Article.objects.filter(title__icontains=ss)
    # 获取右侧热门推荐
    # remen = Article.objects.filter(tui__id=3)[0:6]
    # 获取所有的分类
    # category = Category.objects.all()
    # tags = Tag.objects.all()
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

    # context = {
    #     'article': article,
    #     'remen': remen,
    #     'category': category,
    #     'tags': tags,
    #     'list': list,
    #     'link': link
    # }
    # print(context)

    return render(request, 'search.html', locals())


def about(request):
    # category = Category.objects.all()
    # context = {
    #     'category': category
    # }

    return render(request, 'page.html', locals())

