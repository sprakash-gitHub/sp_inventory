from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': order,
        'form': form,
        'products': products
    }
    return render(request,'dashboard/index.html', context)

@login_required
def staff(request):
    employee = User.objects.all()
    context = {
        'employee': employee,
    }
    return render(request,'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    employee = User.objects.get(id=pk)
    context = {
        'employee': employee,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def product(request):
    items = Product.objects.all()  #using ORM

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added !')
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form,
    }
    return render(request,'dashboard/product.html', context)

@login_required
def product_delete(request, pk):
    items = Product.objects.get(id=pk)
    if request.method=='POST':
        items.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    items = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=items)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request,'dashboard/order.html', context)











