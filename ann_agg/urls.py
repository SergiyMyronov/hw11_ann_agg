from ann_agg import views

from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('author/', views.author, name='author'),
    path('author/<int:num>', views.author_details, name='author_details'),
    path('book/', views.book, name='book'),
    path('book/<int:num>', views.book_details, name='book_details'),
    path('pub/', views.pub, name='pub'),
    path('pub/<int:num>', views.pub_details, name='pub_details'),
    path('store/', views.store, name='store'),
    path('store/<int:num>', views.store_details, name='store_details'),
]
