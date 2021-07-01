from django.urls import path

from ann_agg import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/', views.author, name='author'),
    path('book/', views.book, name='book'),
    path('book/<int:num>', views.book_details, name='book_details'),
    path('pub/', views.pub, name='pub'),
    path('store/', views.store, name='store'),
]
