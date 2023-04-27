import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {"id": 1, "name": "Sally Summers", "email": "sally@summers.com", "hourly_rate": 20},
    {"id": 2, "name": "Wally Winters", "email": "wally@winters.com", "hourly_rate": 15},
    {"id": 3, "name": "Frankie Fall", "email": "frankie@fall.com", "hourly_rate": 10},
]


def get_all_employees():
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        SELECT 
            e.id,
            e.name,
            e.email,
            e.hourly_rate
        FROM employee e
        """
        )
        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(
                row["id"], row["name"], row["email"], row["hourly_rate"]
            )

            employees.append(employee.__dict__)
    return employees


def get_single_employee(id):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            e.id,
            e.name,
            e.email,
            e.hourly_rate
        FROM employee e
        WHERE e.id = ?
        """,
            (id,),
        )

        data = db_cursor.fetchone()

        employee = Employee(
            data["id"], data["name"], data["email"], data["hourly_rate"]
        )

    return employee.__dict__


def create_employee(new_employee):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
            INSERT INTO Employee 
                ( name, email, hourly_rate )
            VALUES 
                ( ?, ?, ? );
            """,
            (
                new_employee["name"],
                new_employee["email"],
                new_employee["hourly_rate"],
            ),
        )
        id = db_cursor.lastrowid

        new_employee["id"] = id

    return new_employee


def delete_employee(id):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM employee
        WHERE id = ?
        """,
            (id,),
        )
