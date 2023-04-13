PRODUCTS = [
    {"id": 1, "name": "IPA", "price": 5},
    {"id": 2, "name": "coffee stout", "price": 6},
]


def get_all_products():
    """GETS ALL PRODUCTS"""
    return PRODUCTS


def get_single_product(id):
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product
