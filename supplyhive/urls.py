from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Import views properly
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core pages
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),

    # Shop
    path("shop/", views.shop, name="shop"),
    path("shop/<slug:slug>/", views.shop, name="shop_by_category"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),  # 👈 NEW

    # Cart
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Billing & Checkout
    path("buy-now/<int:product_id>/", views.buy_now, name="buy_now"),

    path("signin/", views.signin, name="signin"),
      path("register/", views.register, name="register"),  
    path("billing/", views.billing_detail, name="billing_detail"),
    path("checkout/", views.checkout, name="checkout"),

    # Orders
    path("my-orders/", views.my_orders, name="my_orders"),
    path("tracking/<int:order_id>/", views.order_tracking, name="order_tracking"),

    # Search
    path('search/', views.search_view, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
