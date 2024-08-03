"""
URL configuration for candy_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from store_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main_page),

    path('new_raw/', views.new_raw),
    path('new_raw_warehouse/', views.new_raw_warehouse),
    path('new_supplier/', views.new_supplier),
    path('new_product/', views.new_product),
    path('new_prod_warehouse/', views.new_prod_warehouse),
    path('new_customer/', views.new_customer),
    path('new_recipe/', views.new_recipe),
    path('new_doc_raw_in/', views.new_doc_raw_in),
    path('new_doc_raw_in_tab/', views.new_doc_raw_in_tab),
    path('new_doc_prod_in/', views.new_doc_prod_in),
    path('new_doc_prod_in_tab1/', views.new_doc_prod_in_tab1),
    path('new_doc_prod_out/', views.new_doc_prod_out),
    path('new_doc_prod_out_tab/', views.new_doc_prod_out_tab),

    path('show_raws/', views.show_raws),
    path('show_raw_warehouses/', views.show_raw_warehouses),
    path('show_raw_rests/', views.show_raw_rests),
    path('show_suppliers/', views.show_suppliers),
    path('show_products/', views.show_products),
    path('show_prod_warehouses/', views.show_prod_warehouses),
    path('show_customers/', views.show_customers),
    path('show_prod_rests/', views.show_prod_rests),
    path('show_recipes/', views.show_recipes),
    path('show_doc_raw_in/', views.show_doc_raw_in),
    path('show_doc_raw_in/show_selected_doc_raw_in/<int:id>/', views.show_selected_doc_raw_in),
    path('show_doc_prod_in/', views.show_doc_prod_in),
    path('show_doc_prod_in/show_selected_doc_prod_in/<int:id>/', views.show_selected_doc_prod_in),
    path('show_doc_prod_out/', views.show_doc_prod_out),
    path('show_doc_prod_out/show_selected_doc_prod_out/<int:id>/', views.show_selected_doc_prod_out),


    path('new_raw/success/', views.success, kwargs={'category': 'raw'}),
    path('new_raw_warehouse/success/', views.success, kwargs={'category': 'raw_warehouse'}),
    path('new_supplier/success/', views.success, kwargs={'category': 'supplier'}),
    path('new_product/success/', views.success, kwargs={'category': 'product'}),
    path('new_prod_warehouse/success/', views.success, kwargs={'category': 'prod_warehouse'}),
    path('new_customer/success/', views.success, kwargs={'category': 'customer'}),

]
