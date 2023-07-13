from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from appAgro.models import Category
from sayt_dashboard.category.forms import CategoryForm


@staff_member_required(login_url='dashboard-login')
def ctg_list(requests):
    user = requests.user
    if user.is_anonymous:
        return redirect("dashboard-login")
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(requests, 'dashboard/category/list.html', ctx)


@staff_member_required(login_url='dashboard-login')
def ctg_detail(requests, pk):
    ctg = Category.objects.get(pk=pk)
    ctx = {
        'ctg': ctg,
    }
    return render(requests, 'dashboard/category/detail.html', ctx)


@staff_member_required(login_url='dashboard-login')
def ctg_delete(requests, pk):
    ctg = Category.objects.get(pk=pk)
    ctg.delete()
    return redirect('dashboard-ctg-list')


@staff_member_required(login_url='dashboard-login')
def ctg_add(requests):
    forms = CategoryForm()

    if requests.POST:
        form = CategoryForm(requests.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard-ctg-list')

    ctx = {
        "forms": forms

    }
    return render(requests, 'dashboard/category/forms.html', ctx)


@staff_member_required(login_url='dashboard-login')
def ctg_edit(requests, pk):
    root = Category.objects.get(pk=pk)
    forms = CategoryForm(instance=root)

    if requests.POST:
        form = CategoryForm(requests.POST, instance=root)

        if form.is_valid():
            form.save()
            return redirect('dashboard-ctg-list')

    ctx = {
        "forms": forms

    }
    return render(requests, 'dashboard/category/forms.html', ctx)


def ctg_confirm(request, pk):
    root = Category.objects.get(pk=pk)

    ctx = {
        'root': root
    }

    return render(request, "dashboard/category/confirm.html", ctx)
