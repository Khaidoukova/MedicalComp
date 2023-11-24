from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import LabTest
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, labtest_id):
    cart = Cart(request)
    labtest = get_object_or_404(LabTest, id=labtest_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(labtest=labtest,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, labtest_id):
    cart = Cart(request)
    labtest = get_object_or_404(LabTest, id=labtest_id)
    cart.remove(labtest)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

