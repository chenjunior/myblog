from django.conf.urls import url, include


from . import views
urlpatterns = [
    url(r'^', views.index),  # 首页
    url(r'^list-<int:lid>.html/$', views.list),  # 列表页,<int:lid>代表传入一个整型参数
    url(r'^show-<int:sid>.html/$', views.show),  # 详情页,<int:sid>代表传入一个整型参数
    url(r'^tag/<tag>', views.tags),  # 标签列表页
    url(r'^s/$', views.search),  # 搜索列表页
    url(r'^about/$', views.about),  # 列表页
    url(r'list-<int:lid>.html', views.list),  # 列表页
]
