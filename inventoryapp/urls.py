from django.urls import path
from inventoryapp import views
from django.contrib import admin

urlpatterns = [
    path('',views.Home,name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.About, name='about'),
    path('base/', views.Base, name='base'),
    path('bill_base/', views.Bill_base, name='bill_base'),
    path('delete_purchase/', views.Delete_purchase, name='delete_purchase'),
    path('delete_sale/', views.Delete_sale, name='delete_sale'),
    path('delete_stock/', views.Delete_stock, name='delete_stock'),
    path('delete_supplier/', views.Delete_supplier, name='delete_supplier'),
    path('edit_stock/', views.Edit_stock, name='edit_stock'),
    path('edit_supplier/', views.Edit_supplier, name='edit_supplier'),
    path('inventory/', views.Inventory, name='inventory'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('new_purchase/', views.New_purchase, name='new_purchase'),
    path('new_sale/', views.New_sale, name='new_sale'),
    path('purchase_bill/', views.Purchase_bill, name='purchase_bill'),
    path('purchase_list/', views.Purchase_list, name='purchase_list'),
    path('sale_bill/', views.Sale_bill, name='sale_bill'),
    path('sales_list/', views.Sales_list, name='sales_list'),
    path('select_supplier/', views.Select_supplier, name='select_supplier'),
    path('supplier/', views.Supplier, name='supplier'),
    path('suppliers_list/', views.Suppliers_list, name='suppliers_list'),


]