import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from data import add_employee, delete, update, get_by_id, all
from PIL import ImageTk, Image

# Initialize the main application window
app = ctk.CTk()
app.geometry("900x600")
app.minsize(width=900, height=600)
app.maxsize(width=900, height=600)
app.resizable(False, False)
ctk.set_appearance_mode("white")
app.title("Employee Management App")

departments = ["Admin", "Finance", "Student Relationship", "Tutors", "Python", "Cloud Computing", "Web Developers"]

# Function to view employee information
def viewshow_entries():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("300x150")
    new_window.minsize(width=300, height=150)
    new_window.maxsize(width=300, height=150)
    new_window.resizable(False, False)
    ctk.set_appearance_mode("white")
    new_window.title("View Employee")

    viewid_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Employee ID", width=200)
    viewid_entry.pack(pady=5)

    def on_view_employee():
        employee_id = viewid_entry.get()
        employee = get_by_id(employee_id)
        if employee:
            employee_info = f"ID: {employee[0]}\nName: {employee[1]}\nEmployee ID: {employee[2]}\nRole: {employee[3]}\nDepartment: {employee[4]}\nContact: {employee[5]}\nEmail: {employee[6]}"
            messagebox.showinfo("Employee Information", employee_info)
        else:
            messagebox.showerror("Error", "Employee not found.")
    
    viewinfo_button = ctk.CTkButton(new_window, text="View", hover_color="#b01116", command=on_view_employee)
    viewinfo_button.pack(pady=5)

# Function to add a new employee
def addshow_entries():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("300x300")
    new_window.minsize(width=300, height=300)
    new_window.maxsize(width=300, height=300)
    new_window.resizable(False, False)
    ctk.set_appearance_mode("white")
    new_window.title("Add Employee")

    name_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Employee Name", width=200)
    name_entry.pack(pady=5)

    id_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Employee ID", width=200)
    id_entry.pack(pady=5)

    role_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Role", width=200)
    role_entry.pack(pady=5)

    department_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Department", width=200)
    department_entry.pack(pady=5)

    contact_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Contact", width=200)
    contact_entry.pack(pady=5)

    email_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Email", width=200)
    email_entry.pack(pady=5)

    def on_add_employee():
        name = name_entry.get()
        employee_id = id_entry.get()
        role = role_entry.get()
        department = department_entry.get()
        contact = contact_entry.get()
        email = email_entry.get()

        if name and employee_id and role and department and contact and email:
            add_employee(name, employee_id, role, department, contact, email)
            messagebox.showinfo("Success", f"Employee {name} added successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    add_button = ctk.CTkButton(new_window, text="Add Information", hover_color="#b01116", command=on_add_employee)
    add_button.pack(pady=5)

# Function to update employee information
def updateshow_entries():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("300x300")
    new_window.minsize(width=300, height=300)
    new_window.maxsize(width=300, height=300)
    new_window.resizable(False, False)
    ctk.set_appearance_mode("white")
    new_window.title("Update Employee")

    id_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Employee ID", width=200)
    id_entry.pack(pady=5)

    name_entry = ctk.CTkEntry(new_window, placeholder_text="New Employee Name", width=200)
    name_entry.pack(pady=5)

    role_entry = ctk.CTkEntry(new_window, placeholder_text="New Role", width=200)
    role_entry.pack(pady=5)

    department_entry = ctk.CTkEntry(new_window, placeholder_text="New Department", width=200)
    department_entry.pack(pady=5)

    contact_entry = ctk.CTkEntry(new_window, placeholder_text="New Contact", width=200)
    contact_entry.pack(pady=5)

    email_entry = ctk.CTkEntry(new_window, placeholder_text="New Email", width=200)
    email_entry.pack(pady=5)

    def on_update_employee():
        employee_id = id_entry.get()
        name = name_entry.get()
        role = role_entry.get()
        department = department_entry.get()
        contact = contact_entry.get()
        email = email_entry.get()

        if employee_id and (name or role or department or contact or email):
            update(employee_id, name, role, department, contact, email)
            messagebox.showinfo("Success", f"Employee ID {employee_id} updated successfully.")
        else:
            messagebox.showerror("Error", "Employee ID and at least one other field are required.")

    updateinfo_button = ctk.CTkButton(new_window, text="Update Information", hover_color="#b01116", command=on_update_employee)
    updateinfo_button.pack(pady=5)

# Function to delete employee information
def delshow_entries():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("300x150")
    new_window.minsize(width=300, height=150)
    new_window.maxsize(width=300, height=150)
    new_window.resizable(False, False)
    ctk.set_appearance_mode("white")
    new_window.title("Delete Employee")

    viewid_entry = ctk.CTkEntry(new_window, placeholder_text="Enter Employee ID", width=200)
    viewid_entry.pack(pady=5)

    def del_employee():
        employee_id = viewid_entry.get()
        employee = get_by_id(employee_id)

        if employee:
            delete(employee_id)
            messagebox.showinfo("Success", f"Employee ID {employee_id} deleted successfully.")
        else:
            messagebox.showerror("Error", "Employee not found.")

    del_button = ctk.CTkButton(new_window, text="Delete", hover_color="#b01116", command=del_employee)
    del_button.pack(pady=5)

# Function to send email (placeholder function)
def emailshow_entries():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("350x300")
    new_window.minsize(width=350, height=300)
    new_window.maxsize(width=350, height=300)
    new_window.resizable(False, False)
    ctk.set_appearance_mode("white")
    new_window.title("Email")

    from_entry = ctk.CTkEntry(new_window, placeholder_text="From", width=300)
    from_entry.pack(pady=5)

    to_entry = ctk.CTkEntry(new_window, placeholder_text="To", width=300)
    to_entry.pack(pady=5)

    sub_entry = ctk.CTkEntry(new_window, placeholder_text="Subject", width=300)
    sub_entry.pack(pady=5)

    message_entry = ctk.CTkEntry(new_window, placeholder_text="Message", width=300, height=100)
    message_entry.pack(pady=5)

    send_button = ctk.CTkButton(new_window, text="Send Message", hover_color="#b01116")
    send_button.pack(pady=5)

# Function to show department selection
def deptshow_entries():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("350x300")
    new_window.minsize(width=350, height=300)
    new_window.maxsize(width=350, height=300)
    new_window.resizable(False, False)
    ctk.set_appearance_mode("white")
    new_window.title("Departments")

    dept = ctk.CTkComboBox(new_window, values=departments, width=300)
    dept.pack(pady=5)

# Load images
logo = ctk.CTkImage(light_image=Image.open("/Users/user/Desktop/Project/digital fort.png"), size=(250, 130))
img_label = ctk.CTkLabel(app, image=logo, text="")
img_label.place(x=300, y=100)

# Create buttons for main actions
view_button = ctk.CTkButton(app, text="View Employee", hover_color="#b01116", width=250, height=40, command=viewshow_entries)
view_button.place(x=50, y=250)

add_button = ctk.CTkButton(app, text="Add Employee", hover_color="#b01116", width=250, height=40, command=addshow_entries)
add_button.place(x=50, y=300)

update_button = ctk.CTkButton(app, text="Update Employee", hover_color="#b01116", width=250, height=40, command=updateshow_entries)
update_button.place(x=50, y=350)

delete_button = ctk.CTkButton(app, text="Delete Employee", hover_color="#b01116", width=250, height=40, command=delshow_entries)
delete_button.place(x=50, y=400)

email_button = ctk.CTkButton(app, text="Send Email", hover_color="#b01116", width=250, height=40, command=emailshow_entries)
email_button.place(x=50, y=450)

dept_button = ctk.CTkButton(app, text="Departments", hover_color="#b01116", width=250, height=40, command=deptshow_entries)
dept_button.place(x=50, y=500)

# Run the main application loop
app.mainloop()
