import sqlite3

# import json
from models import Product

PRODUCTS = [
    {"id": 1, "name": "IPA", "price": 5},
    {"id": 2, "name": "coffee stout", "price": 6},
]


def get_all_products():
    """Gets all Products from SQL DB"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            p.id,
            p.name,
            p.price
        FROM product p
        """
        )

        products = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            product = Product(row["id"], row["name"], row["price"])
            products.append(product.__dict__)

    return products


# def get_all_products():
#     """GETS ALL PRODUCTS"""
#     return PRODUCTS


def get_single_product(id):
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product
