from django.urls import path
from tasktest2 import views

urlpatterns = [
    path('city/', views.city,  name='city_list'),
    path('city/<int:city_id>/street/', views.street, name='street_list'),
    path('shops/', views.shop, name='shops_list'),
    path('shops/<int:shop_id>/about_shop/', views.about_shop, name='about_shop_list'),
    path('shop/', views.shops),
    path('id_newshop/<int:shop_id>/', views.id_newshop, name='id_newshop'),
]