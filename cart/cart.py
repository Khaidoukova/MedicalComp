from decimal import Decimal
from django.conf import settings
from main.models import LabTest


class Cart:
    def __init__(self, request):
        """Инициализировать корзину."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранить пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart

    def add(self, labtest, quantity=1, override_quantity=False):
        """
        Добавить товар в корзину либо обновить его количество.
        """
        labtest_id = str(labtest.id)
        if labtest_id not in self.cart:
            self.cart[labtest_id] = {'quantity': 0,
                                     'price': str(labtest.price)}
        if override_quantity:
            self.cart[labtest_id]['quantity'] = quantity
        else:
            self.cart[labtest_id]['quantity'] += quantity
        self.save()

    def save(self):
        # пометить сеанс как "измененный",
        # чтобы обеспечить его сохранение
        self.session.modified = True

    def remove(self, labtest):
        """
        Удалить товар из корзины.
        """
        labtest_id = str(labtest.id)
        if labtest_id in self.cart:
            del self.cart[labtest_id]
        self.save()

    def __iter__(self):
        """
        Прокрутить товарные позиции корзины в цикле и
        получить товары из базы данных.
        """
        labtest_ids = self.cart.keys()
        # получить объекты labtest и добавить их в корзину
        labtests = LabTest.objects.filter(id__in=labtest_ids)
        cart = self.cart.copy()
        for labtest in labtests:
            cart[str(labtest.id)]['product'] = labtest
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчитать все товарные позиции в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        # удалить корзину из сеанса
        del self.session[settings.CART_SESSION_ID]
        self.save()
