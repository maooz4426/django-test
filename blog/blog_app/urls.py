# from django.urls import path
# from . import views

# app_name = 'blog_app'
# urlpatterns = [
#    path('', views.index, name='index'),
# ]

from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post_list/', views.PostListView.as_view(), name='post_list'), # ここを追加
]