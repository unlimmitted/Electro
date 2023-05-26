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
    form = Category.objects.all()
    return render(request, 'shop/base.html', context={'title': title, 'category_list': form})


def goods(request):
    title = 'Bads - анти товары'
    search_request = request.GET.get('search', '')

    if search_request:
        form = ProductList.objects.filter(
            Q(title__icontains=search_request) | Q(description__icontains=search_request))
    else:
        form = ProductList.objects.all()

    return render(request, 'shop/goods.html', context={'goods': form, 'title': title})


def category(request, pk):
    title = 'Bads'
    search_request = request.GET.get('search', '')
    selected_category = ProductList.objects.filter(category_id=pk)

    if search_request:
        cat_goods = selected_category.filter(
            Q(title__icontains=search_request) | Q(description__icontains=search_request))
    else:
        cat_goods = selected_category

    return render(request, 'shop/category.html', context={'title': title, 'cat_goods': cat_goods, 'pk': pk})


def cart(request):
    pass


def product(request):
    pass


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
