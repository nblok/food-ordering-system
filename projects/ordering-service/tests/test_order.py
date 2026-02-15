from ordering_service.domain_core.entity.order import Order
from ordering_service.domain_core.valueobject.identifier import OrderId
import uuid


def test_order_id():
    order_id = OrderId(uuid.uuid4())
    order = Order(order_id)
    assert order_id == order.id
