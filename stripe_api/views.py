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
    host = request.get_host()

    item = Item.objects.filter(pk=pk).first()
    if not item:
        return JsonResponse(
            data={'detail': f'Item with id: {pk} not found'}
        )
    line_items = [
        {
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1
        }
    ]

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=f'http://{host}/item/{pk}',
    )

    return JsonResponse(data={'session_id': session.stripe_id})


def get_config(request):
    return JsonResponse(data={
        'public_key': settings.STRIPE_PUBLIC_KEY
    })
