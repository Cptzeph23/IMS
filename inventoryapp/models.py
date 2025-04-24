from django.core.checks import messages
from django.db import models
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from inventoryapp.filters import StockFilter
from inventoryapp.forms import StockForm




class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, verbose_name='Name')
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventoryapp.html'
    paginate_by = 10


class StockCreateView(SuccessMessageMixin,
                      CreateView):  # createview class to add new stock, mixin used to display message
    model = Stock  # setting 'Stock' model as model
    form_class = StockForm  # setting 'StockForm' form as form
    template_name = "edit_stock.html"  # 'edit_stock.html' used as the template
    success_url = '/inventoryapp'  # redirects to 'inventoryapp' page in the url after submitting the form
    success_message = "Stock has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Stock'
        context["savebtn"] = 'Add to Inventory'
        return context


class StockUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit stock, mixin used to display message
    model = Stock  # setting 'Stock' model as model
    form_class = StockForm  # setting 'StockForm' form as form
    template_name = "edit_stock.html"  # 'edit_stock.html' used as the template
    success_url = '/inventoryapp'  # redirects to 'inventoryapp' page in the url after submitting the form
    success_message = "Stock has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Stock'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Stock'
        return context


class StockDeleteView(View):  # view class to delete stock
    template_name = "delete_stock.html"  # 'delete_stock.html' used as the template
    success_message = "Stock has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object': stock})

    def post(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        stock.is_deleted = True
        stock.save()
        messages.success(request, self.success_message)
        return redirect('inventoryapp')

