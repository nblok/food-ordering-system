from common.common_domain.entity.baseentity import BaseEntity
from common.common_domain.valueobject.identifier import ProductId
from common.common_domain.valueobject.money import Money


class Product(BaseEntity[ProductId]):
    def __init__(self, product_id: ProductId, name: str, price: Money):
        super().__init__(product_id)
        self.name = name
        self.price = price