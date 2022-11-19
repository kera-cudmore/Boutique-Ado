from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M5sPQJCYvoXRILPXVKN3HWAoCdVi9rP4sO7hRi9FBDVoL39Ctae5aFSO2eq1GL5mrLFhPWg8FH5LtsRsRk21ymS00sOl1uVn0',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
