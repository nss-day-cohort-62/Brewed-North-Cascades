import sqlite3
import json
from models import Order

ORDERS = [
    {"id": 1, "product_id": 1, "employee_id": 1, "timestamp": "2023-04-12 01:34:12"},
]


def get_all_orders():
    """GETS ALL ORDERS"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            o.id,
            o.product_id,
            o.employee_id,
            o.timestamp
        FROM `Order` o
        """
        )

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(
                row["id"], row["product_id"], row["employee_id"], row["timestamp"]
            )

            orders.append(order.__dict__)
    return orders


def get_single_order(id):
    """GETS A SINGLE ORDER"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            o.id,
            o.product_id,
            o.employee_id,
            o.timestamp
        FROM `Order` o
        WHERE o.id = ?    
        """,
            (id,),
        )

        data = db_cursor.fetchone()

        order = Order(
            data["id"], data["product_id"], data["employee_id"], data["timestamp"]
        )

    return order.__dict__


def create_new_order(order):
    "Function to create new orders"
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order
