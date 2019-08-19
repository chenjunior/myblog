from django.conf.urls import url


from . import views


# app_name = 'blog'
urlpatterns = [
    url(r'^list-(\d+).html/$', views.list, name='list'),  # 列表页
    url(r'^show-(\d+).html/$', views.show, name='show'),  # 详情页
    url(r'^tag/(?P<tag>\w+)', views.tags, name='tags'),  # 标签列表页
    url(r'^s/$', views.search, name='search'),  # 搜索列表页
    url(r'^about/$', views.about, name='about'),  # 关于
    url(r'^', views.index, name='index'),  # 首页
]
