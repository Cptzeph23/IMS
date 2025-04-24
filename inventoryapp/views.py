from django.shortcuts import render, redirect, get_object_or_404




def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Base(request):
    return render(request, 'base.html')

def Bill_base(request):
    return render(request, 'bill_base.html')

def Delete_purchase(request):
    return render(request, 'delete_purchase.html')

def Delete_sale(request):
    return render(request, 'delete_sale.html')

def Delete_stock(request):
    return render(request, 'delete_stock.html')

def Delete_supplier(request):
    return render(request, 'delete_supplier.html')

def Edit_stock(request):
    return render(request, 'edit_stock.html')

def Edit_supplier(request):
    return render(request, 'edit_supplier.html')

def Inventory(request):
    return render(request, 'inventory.html')

def Login(request):
    return render(request, 'login.html')

def Logout(request):
    return render(request, 'logout.html')

def New_purchase(request):
    return render(request, 'new_purchase.html')

def New_sale(request):
    return render(request, 'new_sale.html')

def Purchase_bill(request):
    return render(request, 'purchase_bill.html')

def Purchase_list(request):
    return render(request, 'purchase_list.html')

def Sale_bill(request):
    return render(request, 'sale_bill.html')

def Sales_list(request):
    return render(request, 'sales_list.html')

def Select_supplier(request):
    return render(request, 'select_supplier.html')

def Supplier(request):
    return render(request, 'supplier.html')

def Suppliers_list(request):
    return render(request, 'suppliers_list.html')

