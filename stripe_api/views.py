import stripe
from django.http import JsonResponse
from django.shortcuts import render

from simple_solutions import settings
from stripe_api.models import Item


def get_item(request, pk):
    item = Item.objects.filter(pk=pk).first()

    return render(
        request=request,
        template_name='stripe_api/buy_item.html',
        context={'item': item, 'buy_url': f'/buy/{pk}'}
    )


def buy_item(request, pk):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    item = Item.objects.filter(pk=pk).first()
    if not item:
        return JsonResponse(
            data={'detail': f'Item with id: {pk} not found'}
        )

    payment_intent = stripe.PaymentIntent.create(
        amount=int(item.price) * 100,
        currency=item.currency,
        automatic_payment_methods={
            'enabled': True,
        },
    )

    return JsonResponse(
        data={
            'client_secret': payment_intent['client_secret']
        }
    )


def get_success(request):
    return render(
        request=request,
        template_name='stripe_api/success.html'
    )


def get_config(request):
    return JsonResponse(data={
        'public_key': settings.STRIPE_PUBLIC_KEY
    })
