from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from appAgro.models import Product
from sayt_dashboard.product.forms import ProductForm


@staff_member_required(login_url='dashboard-login')
def list_product(requests):
    product = Product.objects.all()
    ctx = {
        'product': product,
    }

    return render(requests, 'dashboard/product/list.html', ctx)


@staff_member_required(login_url='dashboard-login')
def add_product(requests):
    forms = ProductForm()

    if requests.POST:
        form = ProductForm(requests.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard/product/list.html')

    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/product/forms.html', ctx)


@staff_member_required(login_url='dashboard-login')
def detail_product(requests, pk):
    pro = Product.objects.get(pk=pk)
    ctx = {
        "pro": pro
    }

    return render(requests, 'dashboard/product/detail.html', ctx)


@staff_member_required(login_url='dashboard-login')
def edit_product(requests, pk):
    root = Product.objects.get(pk=pk)
    forms = ProductForm(instance=root)

    if requests.POST:
        form = ProductForm(requests.POST, instance=root)

        if form.is_valid():
            form.save()
            return redirect('dashboard-pro-list')

    ctx = {
        "forms": forms

    }
    return render(requests, 'dashboard/product/forms.html', ctx)


@staff_member_required(login_url='dashboard-login')
def delete_product(requests, pk):
    prod = Product.objects.get(pk=pk)
    prod.delete()
    return redirect('dashboard-pro-list')
