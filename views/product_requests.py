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


def get_single_product(id):
    """GETS A SINGLE PRODUCT"""
    """Filters down all rows in the product table to find the one with matching id"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT 
        p.id,
        p.name,
        p.price
        FROM Product p
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        product = Product(data["id"], data["name"], data["price"])

    return product.__dict__


def create_product(new_product):
    """CREATES A NEW PRODUCT"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO Product 
        (name, price)
        VALUES (? ?);

         """,
            (
                new_product["name"],
                new_product["price"],
            ),
        )

        id = db_cursor.lastrowid

        # Add the `id` property to the product dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_product["id"] = id

    return new_product
