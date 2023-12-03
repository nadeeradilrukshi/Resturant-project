from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('viewcart/', views.view_cart, name='viewcart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('about-us/', views.about_us_template, name='about_us'),
    path('categories/', views.categories_template, name='categories'),
]