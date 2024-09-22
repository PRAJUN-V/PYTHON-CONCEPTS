from enum import Enum, auto

class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()

def get_discounted_price(cart_weight, total_price, discount_type):
    discount_percentage = 0
    if discount_type == DiscountType.STANDARD:
        discount_percentage += 6
    elif discount_type == DiscountType.WEIGHT:
        if cart_weight <= 10:
            discount_percentage += 6
        elif cart_weight > 10:
            discount_percentage += 18
    elif discount_percentage == DiscountType.SEASONAL:
        discount_percentage += 12
    print(total_price)
    print(discount_percentage)
    return total_price - ((discount_percentage/100) * total_price)


print(get_discounted_price(12, 100, DiscountType.WEIGHT))
