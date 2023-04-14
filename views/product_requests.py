PRODUCTS = [
    {"id": 1, "name": "IPA", "price": 5},
    {"id": 2, "name": "coffee stout", "price": 6},
]


def get_all_products():
    """GETS ALL PRODUCTS"""
    return PRODUCTS


def get_single_product(id):
    """GETS A SINGLE PRODUCT"""
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product


def create_product(product):
    """CREATES A NEW PRODUCT"""
    max_id = PRODUCTS[-1]["id"]
    new_id = max_id + 1
    product["id"] = new_id
    PRODUCTS.append(product)

    return product
