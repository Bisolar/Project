import sqlite3

def create_db():
    with sqlite3.connect("employees.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   employee_name TEXT NOT NULL, 
                   employee_id TEXT NOT NULL,
                   role TEXT NOT NULL, 
                   department TEXT, 
                   contact TEXT,
                   email TEXT)
                   ''')

def all():
    with sqlite3.connect("employees.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        return cursor.fetchall()

def get_by_id(employee_id):
    with sqlite3.connect("employees.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
        return cursor.fetchone()

def add_employee(name, employee_id, role, department, contact, email):
    with sqlite3.connect("employees.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO employees (employee_name, employee_id, role, department, contact, email)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, employee_id, role, department, contact, email))
        connection.commit()

def delete(employee_id):
    with sqlite3.connect("employees.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
        connection.commit()
        return "Deleted" if cursor.rowcount > 0 else "No record found"

def update(employee_id, name=None, role=None, department=None, contact=None, email=None):
    with sqlite3.connect("employees.db") as connection:
        cursor = connection.cursor()
        if name:
            cursor.execute("UPDATE employees SET employee_name = ? WHERE employee_id = ?", (name, employee_id))
        if role:
            cursor.execute("UPDATE employees SET role = ? WHERE employee_id = ?", (role, employee_id))
        if department:
            cursor.execute("UPDATE employees SET department = ? WHERE employee_id = ?", (department, employee_id))
        if contact:
            cursor.execute("UPDATE employees SET contact = ? WHERE employee_id = ?", (contact, employee_id))
        if email:
            cursor.execute("UPDATE employees SET email = ? WHERE employee_id = ?", (email, employee_id))
        connection.commit()
        return "Updated" if cursor.rowcount > 0 else "No record found"

if __name__ == '__main__':
    create_db()
