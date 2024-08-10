# import sqlite3
import customtkinter 
# from tkinter import *
from tkinter import ttk, messagebox
# from tkmacosx import Button
from PIL import ImageTk, Image

# connection = sqlite3.connect('employee_management.db')
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
#                id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                employee_name TEXT NOT NULL, 
#                employee_id TEXT NOT NULL,
#                role TEXT NOT NULL, 
#                department TEXT, 
#                contact TEXT
#                 email TEXT)
#                ''')

# def add_employee(name, employee_id, role, department, contact, email):
#     try:
#         cursor.execute('''
#         INSERT INTO employees (name, employee_id, role, department, contact, email)
#         VALUES (?, ?, ?, ?, ?, ?)
#         ''', (name, employee_id, role, department, contact, email))
#         connection.commit()
#         messagebox.showinfo("Success", f"Employee {name} added successfully.")
#     except sqlite3.IntegrityError:
#         messagebox.showerror("Error", "Employee ID must be unique.")

# def view_employee(employee_id):
#     cursor.execute('SELECT * FROM employees WHERE employee_ID = ?', (employee_id,))
#     employee = cursor.fetchone()
#     if employee:
#         messagebox.showinfo("Employee Details", f"""
#         ID: {employee[0]}
#         Name: {employee[1]}
#         Employee ID: {employee[2]}
#         Role: {employee[3]}
#         Department: {employee[4]}
#         Contact: {employee[5]}
#         Email: {employee[6]}
#         """)
#     else:
#         messagebox.showinfo("Error", "Employee not found.")

# def on_add_employee():
#     name = entry_name.get()
#     employee_id = entry_employee_id.get()
#     role = entry_role.get()
#     department = entry_department.get()
#     contact = entry_contact.get()
#     email = entry_email.get()
#     if name and employee_id and role and department and contact and email:
#         add_employee(name, employee_id, role, department, contact, email)
#         entry_name.delete(0, tk.END)
#         entry_employee_id.delete(0, tk.END)
#         entry_role.delete(0, tk.END)
#         entry_department.delete(0, tk.END)
#         entry_contact.delete(0, tk.END)
#         entry_email.delete(0, tk.END)
#     else:
#         messagebox.showerror("Error", "All fields are required.")

# def on_view_employee():
#     employee_id = entry_search_employee_id.get()
#     if employee_id:
#         view_employee(employee_id)
#     else:
#         messagebox.showerror("Error", "Employee ID is required.")

root = customtkinter.CTk()
root.minsize(width=900, height=600)
root.maxsize(width=900, height=600)
customtkinter.set_appearance_mode("White")
root.title("Employee Management App")

logo_path = "/Users/user/Desktop/Project/digital fort.png"
logo = Image.open(logo_path)
logo = ImageTk.PhotoImage(logo)

Frame1 = customtkinter.CTkFrame(root, background='#b01116')
Frame1.place(x=0, y=0, relwidth= 0.2, relheight= 1)

frame_add = customtkinter.CTkFrame(root, background="Light Grey")
frame_add.place(x=200, y=45, relwidth=0.35, relheight=0.4)

frame_view = customtkinter.CTkFrame(root, background="Light Blue")
frame_view.place(x=540, y=45, relwidth=0.35, relheight=0.4)

frame_other = customtkinter.CTkFrame(root, background="Light Green")
frame_other.place(x=200, y=300, relwidth=0.35, relheight=0.4)

frame_other1 = customtkinter.CTkFrame(root, background="Grey")
frame_other1.place(x=540, y=300, relwidth=0.35, relheight=0.4)

# Create a label to display the logo
logo_label = customtkinter.CTkLabel(Frame1, image=logo, bg= '#b01116')
logo_label.place(x=0, y=0)
#create menu icons
department_label= customtkinter.CTkLabel(Frame1, text="🏬 Departments", background="#b01116", foreground= "White", font= ("Arial", 14, "bold"))
department_label.place(x=20, y = 20, relx= 0.0, rely=0.2)

view_label= customtkinter.CTkLabel(Frame1, text="👔 View Employee", background="#b01116", foreground= "White", font= ("Arial", 14, "bold"))
view_label.place(x=20, y = 70, relx= 0.0, rely=0.2)

add_label= customtkinter.CTkLabel(Frame1, text="➕ Add Employee", background="#b01116", foreground= "White", font= ("Arial", 14, "bold"))
add_label.place(x=20, y = 120, relx= 0.0, rely=0.2)

email_label= customtkinter.CTkLabel(Frame1, text="📩 Send Email", background="#b01116", foreground= "White", font= ("Arial", 14, "bold"))
email_label.place(x=20, y = 170, relx= 0.0, rely=0.2)

update_label= customtkinter.CTkLabel(Frame1, text="✅ Update Employee", background="#b01116", foreground= "White", font= ("Arial", 14, "bold"))
update_label.place(x=20, y = 220, relx= 0.0, rely=0.2)

leave_label= customtkinter.CTkLabel(Frame1, text="🆎 Leave Activity", background="#b01116", foreground= "White", font= ("Arial", 14, "bold"))
leave_label.place(x=20, y = 270, relx= 0.0, rely=0.2)
# create add employee form
add_title = customtkinter.CTkLabel(frame_add, text="Add Employee", background="Light Grey")
add_title.grid(row=0, column=0, columnspan=2, pady=5)

name= customtkinter.CTkLabel(frame_add, text="Name:", background="Light Grey")
name.grid(row=1, column=0)
entry_name = customtkinter.Entry(frame_add)
entry_name.grid(row=1, column=1)

id= customtkinter.CTkLabel(frame_add, text="Employee ID:", background="Light Grey")
id.grid(row=2, column=0)
entry_employee_id = ttk.Entry(frame_add)
entry_employee_id.grid(row=2, column=1)

department= customtkinter.CTkLabel(frame_add, text="Department:", background="Light Grey")
department.grid(row=3, column=0)
entry_department = ttk.Entry(frame_add)
entry_department.grid(row=3, column=1)

role= customtkinter.CTkLabel(frame_add, text="Role:", background="Light Grey")
role.grid(row=4, column=0)
entry_role = ttk.Entry(frame_add)
entry_role.grid(row=4, column=1)

contact= customtkinter.CTkLabel(frame_add, text="Contact:", background="Light Grey")
contact.grid(row=5, column=0)
entry_contact = ttk.Entry(frame_add)
entry_contact.grid(row=5, column=1)

email= customtkinter.CTkLabel(frame_add, text="Email:", background="Light Grey")
email.grid(row=6, column=0)
entry_email = ttk.Entry(frame_add)
entry_email.grid(row=6, column=1)

add_button= customtkinter.CTkButton(frame_add, text="Add Employee")
add_button.grid(row=7, column=0, columnspan=2, pady=10)

# View employee form
view= customtkinter.CTkLabel(frame_view, text="View Employee", background="Light Blue")
view.grid(row=0, column=0, columnspan=2, pady=5)

search= customtkinter.CTkLabel(frame_view, text="Employee ID:", background="Light Blue")
search.grid(row=1, column=0)
entry_search_employee_id = ttk.Entry(frame_view)
entry_search_employee_id.grid(row=1, column=1)

view_button= customtkinter.CTkButton(frame_view, text="View Employee", background="Light Blue")
view_button.grid(row=2, column=0, columnspan=2, pady=10)

# create update employee form
add_title1 = customtkinter.CTkLabel(frame_other1, text="Update Employee", background="Grey")
add_title1.grid(row=0, column=0, columnspan=2, pady=5)

name= customtkinter.CTkLabel(frame_other1, text="Name:", background="Grey")
name.grid(row=1, column=0)
entry_name = ttk.Entry(frame_other1)
entry_name.grid(row=1, column=1)

id= customtkinter.CTkLabel(frame_other1, text="Employee ID:", background="Grey")
id.grid(row=2, column=0)
entry_employee_id = ttk.Entry(frame_other1)
entry_employee_id.grid(row=2, column=1)

department= customtkinter.CTkLabel(frame_other1, text="Department:", background="Grey")
department.grid(row=3, column=0)
entry_department = ttk.Entry(frame_other1)
entry_department.grid(row=3, column=1)

role= customtkinter.CTkLabel(frame_other1, text="Role:", background="Grey")
role.grid(row=4, column=0)
entry_role = ttk.Entry(frame_other1)
entry_role.grid(row=4, column=1)

contact= customtkinter.CTkLabel(frame_other1, text="Contact:", background="Grey")
contact.grid(row=5, column=0)
entry_contact = ttk.Entry(frame_other1)
entry_contact.grid(row=5, column=1)

email= customtkinter.CTkLabel(frame_other1, text="Email:", background="Grey")
email.grid(row=6, column=0)
entry_email = ttk.Entry(frame_other1)
entry_email.grid(row=6, column=1)

add_button= customtkinter.CTkButton(frame_other1, text="Update Employee")
add_button.grid(row=7, column=0, columnspan=2, pady=10)

#View employee department form
view_department= customtkinter.CTkLabel(frame_other, text="View Department", background="Light Green")
view_department.grid(row=0, column=0, columnspan=2, pady=5)

search_department= customtkinter.CTkLabel(frame_other, text="Employee ID:", background="Light Green")
search_department.grid(row=1, column=0)
entry_search_employee_id = ttk.Entry(frame_other)
entry_search_employee_id.grid(row=1, column=1)

view_button= customtkinter.CTkButton(frame_other, text="View Employee", background="Light Green")
view_button.grid(row=2, column=0, columnspan=2, pady=10)
#send email 
send_email= customtkinter.CTkLabel(frame_other, text="Send Email", background="Light Green")
send_email.grid(row=4, column=0, columnspan=2, pady=5)

email= customtkinter.CTkLabel(frame_other, text="Employee ID:", background="Light Green")
email.grid(row=5, column=0)
entry_search_employee_id = ttk.Entry(frame_other)
entry_search_employee_id.grid(row=5, column=1)

email_button= customtkinter.CTkButton(frame_other, text="View Employee", background="Light Blue")
email_button.grid(row=6, column=0, columnspan=2, pady=10)


root.mainloop()
# connection.commit()
# connection.close()