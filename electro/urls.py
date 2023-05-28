"""electro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eshop.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/<int:pk>', category, name='category'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('product/<str:slug>', product_page, name='product_page'),
    path('all-product/', store, name='all_product'),
    path('logout/', logout_user, name='logout'),
    path('addtocart/<str:slug>/', add_to_cart, name='add_to_cart'),
    path('delete_cart_item/<str:slug>', delete_cart_item, name='delete_cart_item'),
    path('cart/<str:username>/', cart, name='user_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
