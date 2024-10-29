from django.shortcuts import render, redirect
from .models import Product,Log
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})
def creates(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            Log.objects.create(
                type='create',
                product=product,
                message=f'New product created: {product.title} (ID: {(Product.id)})'
            )
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'main/create.html', {'form': form})
def update(request,id):
    product = Product.objects.get(id=id)
    old_name = product.title
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            Log.objects.create(
                type='update',
                product=product,
                message=f'Updated product {id}: old name={old_name}, new name={product.title}'
            )
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'main/update.html', {'form': form})
def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_list')