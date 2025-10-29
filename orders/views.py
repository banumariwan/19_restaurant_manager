from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from .models import MenuItem, Order, Table
from .forms import MenuItemForm, OrderForm


# 🔐 Authentication
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'orders/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('orders_list')
    else:
        form = AuthenticationForm()
    return render(request, 'orders/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


# 🍽️ Menu management
@login_required
def menu_list(request):
    query = request.GET.get('q', "")
    sort = request.GET.get('sort', "name")

    menu_items = MenuItem.objects.all()

    if query:
        menu_items = menu_items.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query)  # fixed typo: categories -> category
        )

    if sort in ['name', '-name', 'price', '-price', 'category', '-category']:
        menu_items = menu_items.order_by(sort)

    return render(request, 'orders/menu_list.html', {'menu_items': menu_items, 'query': query, 'sort': sort})


@login_required
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')  # ✅ Fixed
    else:
        form = MenuItemForm()
    return render(request, 'orders/add_menu_item.html', {'form': form})


@login_required
def update_menu_item(request, id):
    menu_item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')  # ✅ Fixed
    else:
        form = MenuItemForm(instance=menu_item)
    return render(request, 'orders/update_menu_item.html', {'form': form})


@login_required
def delete_menu_item(request, id):
    menu_item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        menu_item.delete()
        return redirect('menu_list')  # ✅ Fixed
    return render(request, 'orders/delete_menu_item.html', {'menu_item': menu_item})


# 🧾 Orders management
@login_required
def order_list(request):
    query = request.GET.get('q', "")
    status_filter = request.GET.get('status', "")
    sort = request.GET.get('sort', "created_by")

    orders = Order.objects.select_related("table", "created_by").prefetch_related("items")

    if query:
        orders = orders.filter(
            Q(table__number__icontains=query) |
            Q(items__name__icontains=query)  # fixed: item -> items
        ).distinct()

    if status_filter:
        orders = orders.filter(status=status_filter)

    if sort in ['created_by', '-created_by', 'total_price', '-total_price', 'status', '-status']:
        orders = orders.order_by(sort)

    return render(request, 'orders/orders_list.html', {
        'orders': orders,
        'query': query,
        'status_filter': status_filter,
        'sort': sort,
    })


@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user
            order.save()
            form.save_m2m()

            # Calculate total price
            total = order.items.aggregate(total=Sum('price'))['total']
            order.total_price = total or 0
            order.save()
            return redirect('orders_list')  # ✅ Fixed
    else:
        form = OrderForm()
    return render(request, 'orders/add_order.html', {'form': form})


@login_required
def update_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            form.save_m2m()

            # Recalculate total
            total = order.items.aggregate(total=Sum('price'))['total']
            order.total_price = total or 0
            order.save()
            return redirect('orders_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/update_order.html', {'form': form, 'order': order})


@login_required
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('orders_list')
    return render(request, 'orders/delete_order.html', {'order': order})
