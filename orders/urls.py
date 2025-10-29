from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/update/<int:id>/', views.update_menu_item, name='update_menu_item'),
    path('menu/delete/<int:id>/', views.delete_menu_item, name='delete_menu_item'),


    path('orders/', views.order_list, name='orders_list'),
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/update/<int:id>/', views.update_order, name='update_order'),
    path('orders/delete/<int:id>/', views.delete_order, name='delete_order'),
]
