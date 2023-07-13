from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from appAgro.models import Category, Product, ProdImg
from appAgro.services import search_products
from sayt_dashboard.models import User


@staff_member_required(login_url="register")
def index(request):
    ctgs = Category.objects.all()
    prod = Product.objects.all()

    user = request.user
    print(request.user)

    if user.is_anonymous:
        return redirect('agrologin')

    traktor = Category.objects.get(slug='traktorla')
    traktors = Product.objects.filter(ctg=traktor)

    data = []
    for i in traktors:
        try:
            data.append({
                "id": i.id,
                "img": ProdImg.objects.filter(prod_id=i.id).first()
            })
        except:
            pass
    ctx = {
        'ctgs': ctgs,
        "prod": prod,
        "data": data,
        'home': True,
        'traktors': traktors
    }
    if not user.is_staff:
        ctx['staff'] = False
    else:
        ctx['staff'] = True

    return render(request, 'sayt/index.html', ctx)


def category(request, slug=None, ):
    ctgs = Category.objects.all()
    category = True
    prods = Product.objects.all().order_by("-pk")
    ctg = None
    search = request.GET.get('search', None)

    if search:
        prods = search_products(search)

    if slug:
        ctg = Category.objects.get(slug=slug)
        prods = Product.objects.filter(ctg=ctg)

    ctx = {
        "ctgs": ctgs,
        "category": category,
        "prods": prods,
        "ctg": ctg,
    }

    return render(request, 'sayt/category.html', ctx)


def views(request, pk):
    ctg = Category.objects.all()
    prod = Product.objects.get(pk=pk)
    imgs = ProdImg.objects.filter(prod=prod)

    prods = Product.objects.all().order_by('-pk')

    ctx = {
        'ctg': ctg,
        'prod': prod,
        "imgs": imgs,
        'prods': prods
    }

    return render(request, 'sayt/views.html', ctx)


def register(request):
    if request.POST:
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get("password")
        password_conf = request.POST.get('password_conf')

        if password == password_conf:
            return render(request, 'sayt/register.html')

        user = User()
        user.name = name
        user.username = username
        user.set_password(password)
        user.save()

        login(request, user)
        authenticate(request)
        return redirect('home')

    return render(request, 'sayt/register.html')


def agrologin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = User.objects.filter(username=username).first()

        print("USEr, ", user)
        print("USEr, ", request.POST)

        if not user:
            ctx = {
                "error": True
            }
            return render(request, "sayt/register.html", ctx)
        print("USEr, ", password)

        if not user.check_password(password):
            ctx = {
                "error": True
            }
            return render(request, "sayt/register.html", ctx)
        login(request, user)
        authenticate(request)
        return redirect('home')
    return render(request, 'sayt/register.html')
