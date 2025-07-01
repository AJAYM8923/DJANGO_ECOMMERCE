
"""
URL configuration for ekart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_cartitem/<int:id>/', views.delete_cartitem, name='delete_cartitem'),
    path('update_account/', views.update_account, name='update_account'),
    path('confirm_address/', views.confirm_address, name='confirm_address'),
    path('place_order/', views.place_order, name='place_order'),
    path('product_details/<int:id>/',views.product_details,name="product_details"),
    path('search/', views.search_products, name='search_products'),
    path('contact/',views.contact,name="contact"),
    path('stripe_payment/', views.stripe_payment, name='stripe_payment'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # Add these paths
  
    path('admin_add_product/', views.admin_add_product, name='admin_add_product'),
    path('admin_edit_product/<int:id>/', views.admin_edit_product, name='admin_edit_product'),
    path('admin_delete_product/<int:id>/', views.admin_delete_product, name='admin_delete_product'),
    path('admin_delete_user/<int:id>/', views.admin_delete_user, name='admin_delete_user'),
    path('admin_update_order_status/<int:id>/', views.admin_update_order_status, name='admin_update_order_status'),
    path('admin_delete_contact/<int:id>/', views.admin_delete_contact, name='admin_delete_contact'),
    path('add-collection/', views.admin_add_collection, name='admin_add_collection'),
    path('collections/edit/<int:id>/', views.admin_edit_collection, name='admin_edit_collection'),
    path('collections/delete/<int:id>/', views.admin_delete_collection, name='admin_delete_collection'),
   





 





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""