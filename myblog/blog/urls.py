from django.conf.urls import url, include

from . import views
urlpatterns = [
    url(r'^', views.index),  # 首页
    url(r'^news/$', views.news),  # 新闻
    url(r'^bbs/$', views.bbs),  # 论坛

]
