import pytest

# from decimal import Decimal
# from ..models import Item, Order
from .factories import ItemFactory

pytestmark = pytest.mark.django_db


''' def test___str__(product):
    order = Order.objects.create(
        cpf="401.142.450-10",
        name="Fulano",
        email="test@fulano.com",
        postal_code="76900-649",
        address="Rua Castro Alves",
        number="123",
        district="Jardim dos Migrantes",
        state="RO",
        city="Ji-Paraná",
    ) '''
def test___str__(product, order, item):
    assert order.__str__() == f"Pedido {order.id}"
    assert str(order) == f"Pedido {order.id}"

    ''' item = Item.objects.create(
        order=order,
        product=product,
        price=Decimal(10),
        quantity=1,
    ) '''

    assert item.__str__() == str(item.id)
    assert str(item) == str(item.id)

def test_order_get_total_price(order):
    item = ItemFactory(order=order)
    item2 = ItemFactory(order=order)
    assert (
        order.get_total_price()
        == item.quantity * item.price + item2.quantity * item2.price
    )


def test_order_get_description(order):
    item = ItemFactory(order=order, quantity=2)
    assert order.get_description() == f"2x {item.product.name}"


def test_item_get_total_price():
    item = ItemFactory(quantity=2)
    assert item.get_total_price() == 2 * item.price