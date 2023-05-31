from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from eshop.forms import *
from eshop.utils import *
from eshop.models import *
from django.db.models import Q
# Create your views here.


def home(request):
    title = 'Electro'
    quantity_form = AddToCart(request.POST)
    category = Category.objects.all()
    products = ProductList.objects.all()
    return render(request, 'shop/base.html', context={'title': title, 'category_list': category, 'products': products, 'quantity_form': quantity_form})


def store(request):
    quantity_form = AddToCart(request.POST)
    search_request = request.GET.get('search', '')

    if search_request:
        all_products = ProductList.objects.filter(
            Q(title__icontains=search_request) | Q(description__icontains=search_request) | Q(full_description__icontains=search_request))
    else:
        all_products = ProductList.objects.all

    return render(request, 'shop/store.html', context={'all_products': all_products, 'quantity_form': quantity_form})


def product_page(request, slug):
    product = ProductList.objects.filter(slug=slug)
    return render(request, 'shop/product.html', context={'product': product})


def category(request, pk):
    title = 'Bads'
    quantity_form = AddToCart(request.POST)
    search_request = request.GET.get('search', '')
    selected_category = ProductList.objects.filter(category_id=pk)

    if search_request:
        cat_goods = selected_category.filter(
            Q(title__icontains=search_request) | Q(description__icontains=search_request))
    else:
        cat_goods = selected_category

    return render(request, 'shop/category.html', context={'title': title, 'cat_goods': cat_goods, 'pk': pk, 'quantity_form': quantity_form})


def cart(request, username):
    products = []
    names = UserCartList.objects.all()

    for n in names:
        if n.username == username:
            products.append(ProductList.objects.filter(slug=n.product))
    return render(request, 'shop/cart.html', context={'data': products, 'title': 'Корзина - Nimble'})


def delete_cart_item(request, slug):
    del_item = UserCartList.objects.filter(product=slug)
    del_item.delete()

    return redirect('user_cart', request.user.username)


def add_to_cart(request, slug):
    form = AddToCart(request.POST)

    if form.is_valid():
        cart_data = form.save(commit=False)
        cart_data.username = request.user.username
        cart_data.product = slug
        cart_data.save()
    # return redirect('user_cart', request.user.username)
    return redirect('home')


def checkout(request, slug):
    from_db = ProductList.objects.filter(slug=slug)
    return render(request, 'shop/checkout.html', context={'prod_info': from_db})


def logout_user(request):
    logout(request)
    return redirect('home')


class LoginUser(DataMixin, LoginView):
    # LoginUserForm стандартная форма входа из коробки с Django
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Вход пользователя - Electro")
        return dict(list(context.items()) + list(c_def.items()))

    # Если форма была заполнена корректно,
    # перенаправляет в каталог
    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    # RegisterUserForm стандартная форма регистрации из коробки с Django
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Регистрация пользователя - Electro")
        return dict(list(context.items()) + list(c_def.items()))

    # Если форма была заполнена корректно,
    # входит и перенаправляет в каталог
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
