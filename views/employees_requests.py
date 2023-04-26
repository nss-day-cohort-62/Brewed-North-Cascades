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


def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1
    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
