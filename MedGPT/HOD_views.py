import pytz
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from app.models import Product, SoldItem
from app.forms import SellProductForm, SoldItemForm  # Assuming you create a form for selling products
@login_required
def product_list(request):
    local_tz = pytz.timezone('Asia/Tashkent')  # UTC +5
    local_time = timezone.now().astimezone(local_tz)

    today = local_time.date()
    products = Product.objects.all()
    products_count = Product.objects.count()
    products_left_count = Product.objects.filter(quantity=0).count()
    sold_items_count = SoldItem.objects.filter(sold_at__date=today).count
    nasiya_sold_items = SoldItem.objects.filter(payment_type='online').count

    return render(request, 'Hod/product_list.html', {'products': products, 'products_count': products_count, 'sold_items_count': sold_items_count, 'nasiya_count': nasiya_sold_items, 'products_left': products_left_count})

def list_sold_items(request):
    local_tz = pytz.timezone('Asia/Tashkent')  # UTC +5

    # Get the current time in the local timezone
    local_time = timezone.now().astimezone(local_tz)

    # Get the local date
    today = local_time.date()

    print(f"Today's local date: {today}")  # Debug print statement

    # Filter sold items by the local date
    sold_items = SoldItem.objects.filter(sold_at__date=today)

    print(f"Sold items today: {sold_items}")  # Debug print statement

    return render(request, 'Hod/list_sold_items.html', {'sold_items': sold_items})
@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'Hod/product_detail.html', {'product': product})
@login_required
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        Product.objects.create(name=name, description=description, quantity=quantity, price=price)
        return redirect('product_list')
    return render(request, 'Hod/product_form.html')
@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.quantity = request.POST.get('quantity')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_list')
    return render(request, 'Hod/product_form.html', {'product': product})
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'Hod/product_edit.html', {'product': product})

@login_required
def sell_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = SellProductForm(request.POST)
        if form.is_valid():
            quantity_sold = form.cleaned_data['quantity_sold']
            payment_type = form.cleaned_data['payment_type']
            comment = form.cleaned_data['comment']
            if quantity_sold <= product.quantity:
                SoldItem.objects.create(
                    product=product,
                    quantity_sold=quantity_sold,
                    payment_type=payment_type,
                    comment=comment
                )
                product.quantity -= quantity_sold
                product.save()
                messages.success(request, 'Sotildi')
                return redirect('product_list')
    else:
        form = SellProductForm()

    return render(request, 'Hod/sell_product.html', {'form': form, 'product': product})

def nasiya_sold_items(request):
    sold_items = SoldItem.objects.filter(payment_type='online')
    return render(request, 'Hod/nasiya_sold_items.html', {'sold_items': sold_items})


def edit_sold_item(request, pk):
    sold_item = get_object_or_404(SoldItem, pk=pk)
    if request.method == 'POST':
        form = SoldItemForm(request.POST, instance=sold_item)
        if form.is_valid():
            form.save()
            return redirect('nasiya_sold_items')
    else:
        form = SoldItemForm(instance=sold_item)

    return render(request, 'Hod/edit_sold_item.html', {'form': form, 'sold_item': sold_item})

def out_of_stock_products(request):
    products = Product.objects.filter(quantity=0)
    return render(request, 'Hod/out_of_stock_products.html', {'products': products})

def today_sales_report(request):
    # Define your local timezone
    local_tz = pytz.timezone('Asia/Tashkent')  # UTC +5

    # Get the current time in the local timezone
    local_time = timezone.now().astimezone(local_tz)

    # Get the local date
    today = local_time.date()

    # Filter sold items by the local date
    sold_items = SoldItem.objects.filter(sold_at__date=today)

    # Calculate the total price
    total_price = sum(item.product.price * item.quantity_sold for item in sold_items)

    return render(request, 'Hod/today_sales_report.html', {
        'sold_items': sold_items,
        'total_price': total_price,
    })
