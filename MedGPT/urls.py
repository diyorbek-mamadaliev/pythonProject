from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,HOD_views
from .views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    # Login Path
    path('Login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('register/', register, name='register'),
    # Main
path('', HOD_views.product_list, name='product_list'),
    path('product/<int:pk>/', HOD_views.product_detail, name='product_detail'),
    path('product/new/', HOD_views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', HOD_views.product_edit, name='product_edit'),
    path('sold-items/', HOD_views.list_sold_items, name='list_sold_items'),
    path('today-sales-report/', HOD_views.today_sales_report, name='today_sales_report'),
    path('out-of-stock/', HOD_views.out_of_stock_products, name='out_of_stock_products'),
    path('nasiya-sold-items/', HOD_views.nasiya_sold_items, name='nasiya_sold_items'),
    path('sold_items/edit/<int:pk>/', HOD_views.edit_sold_item, name='edit_sold_item'),
    path('product/<int:pk>/delete/', HOD_views.product_delete, name='product_delete'),
    path('product/<int:pk>/sell/', HOD_views.sell_product, name='sell_product'),

    # Profile
    path('profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
