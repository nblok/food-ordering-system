import uuid
from order_service.order_domain.domain_core.entity.order import Order
from common.common_domain.valueobject.identifier import OrderId


def test_order_id():
    order_id = OrderId(uuid.uuid4())
    order = Order(order_id)
    assert order_id == order.id
