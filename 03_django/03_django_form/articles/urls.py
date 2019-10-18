from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete', views.detail, name='delete'),
    path('<int:article_pk>/update', views.detail, name='update'),
    path('<int:article_pk>/comments', views.detail, name='update'),
    path('<int:article_pk>/comments', views.detail, name='update'),

]
