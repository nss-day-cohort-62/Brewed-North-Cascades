EMPLOYEES = [
    {"id": 1, "name": "Sally Summers", "email": "sally@summers.com", "hourly_rate": 20},
    {"id": 2, "name": "Wally Winters", "email": "wally@winters.com", "hourly_rate": 15},
    {"id": 3, "name": "Frankie Fall", "email": "frankie@fall.com", "hourly_rate": 10},
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    """Gets a single employee

    Args:
        id (int): Integer listed as Id

    Returns:
        __dict__: employee
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee


def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1
    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def delete_employee():
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
