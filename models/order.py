class Order:
    """A member of Brewed-North-Cascades. Stores all currently relevant data for our Order Class in fields."""

    def __init__(self, id, product_id, employee_id, timestamp):
        self.id = id
        self.product_id = product_id
        self.employee_id = employee_id
        self.timestamp = timestamp
