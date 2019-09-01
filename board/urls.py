# blog/urls.py
from django.urls import path

from . import views
from . import views_cbv

app_name = 'board'

urlpatterns = [
    path('', views_cbv.post_list, name='post_list'),
    path('<int:pk>/', views_cbv.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
    path('comments/', views.comment_list, name='comment_list'),
    path('cbv/new/', views_cbv.post_new),
    path('cbv/<int:pk>/edit/', views_cbv.post_edit),
    path('cbv/<int:pk>/delete/', views_cbv.post_delete),
]
