ORDERS = [
    {"id": 1, "product_id": 1, "employee_id": 1, "timestamp": "2023-04-12 01:34:12"},
]


def get_all_orders():
    """GETS ALL ORDERS"""
    return ORDERS


def get_single_order(id):
    """GETS A SINGLE ORDER"""
    requested_orders = None
    for order in ORDERS:
        if order["id"] == id:
            requested_orders = order
            return requested_orders


def create_new_order(order):
    "Function to create new orders"
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order
