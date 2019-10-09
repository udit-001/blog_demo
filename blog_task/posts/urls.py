from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('create/', views.post_create, name='create'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail')
]
