from django.urls import path
from .views import CartItemViews
from .views import CartItemsList

urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items-list/', CartItemsList.as_view())
]
