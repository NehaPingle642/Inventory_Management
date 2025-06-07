from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'core/add_product.html', {'form': form})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm(instance=product)
    return render(request, 'core/edit_product.html', {'form': form})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Changed from '/' to 'product_list'
    return render(request, 'core/delete_product.html', {'product': product})