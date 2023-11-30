from django.urls import path

from stripe_api.views import get_item, buy_item, get_config, get_success

app_name = 'stripe_api'

urlpatterns = [
    path('item/<int:pk>/', get_item, name='get_item'),
    path('buy/<int:pk>/', buy_item, name='buy_item'),

    path('buy/success/', get_success, name='get_success'),
    path('config/', get_config, name='get_config')
]
