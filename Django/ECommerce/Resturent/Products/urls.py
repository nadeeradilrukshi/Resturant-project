from django.urls import path
from .views import (
    home1,
    view_cart,
    add_to_cart,
    remove_from_cart,
    about_us_template,
    categories_template,
    homepage,
    items,
    signup,
    logout_view,
)

urlpatterns = [
    path('', home1, name='home'),
    path('viewcart/', view_cart, name='viewcart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('about-us/', about_us_template, name='about_us'),
    path('categories/', categories_template, name='categories'),
    path('homepage/', homepage, name='homepage'),
    path('items/', items, name='items'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),  # Use your custom logout view
]

