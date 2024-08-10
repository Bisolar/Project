import customtkinter
from data import add, delete, update, get_by_id, all

app = customtkinter.CTk()

app.minsize(width=900, height=600)
app.maxsize(width=900, height=600)
customtkinter.set_appearance_mode("White")
app.title("Employee Management App")

# Function to add a passcode
def add_passcode():
    code = passcode_entry.get()
    add(code)
    print(f"Added: {code}")
    passcode_entry.delete(0, 'end')

# Function to delete a passcode by ID
def delete_passcode():
    id_to_delete = id_entry.get()
    delete(id_to_delete)
    print(f"Deleted ID: {id_to_delete}")
    id_entry.delete(0, 'end')

# Function to update a passcode by ID
def update_passcode():
    new_code = new_passcode_entry.get()
    id_to_update = id_entry.get()
    update(new_code, id_to_update)
    print(f"Updated ID: {id_to_update} with new passcode: {new_code}")
    new_passcode_entry.delete(0, 'end')
    id_entry.delete(0, 'end')

# Function to get a passcode by ID
def get_passcode():
    id_to_get = id_entry.get()
    result = get_by_id(id_to_get)
    print(f"Passcode for ID {id_to_get}: {result}")
    id_entry.delete(0, 'end')

# Function to get all passcodes
def get_all_passcodes():
    result = all()
    print("All passcodes: ", result)

# Entry for passcode
passcode_entry = customtkinter.CTkEntry(app, placeholder_text="Enter your passcode", show="*", width=200)
passcode_entry.pack(pady=5)

# Button to add passcode
add_button = customtkinter.CTkButton(app, text="Add Passcode", command=add_passcode)
add_button.pack(pady=5)

# Entry for ID
id_entry = customtkinter.CTkEntry(app, placeholder_text="Enter ID", width=200)
id_entry.pack(pady=5)

# Entry for new passcode (for update operation)
new_passcode_entry = customtkinter.CTkEntry(app, placeholder_text="Enter new passcode", show="*", width=200)
new_passcode_entry.pack(pady=5)

# Button to delete passcode
delete_button = customtkinter.CTkButton(app, text="Delete Passcode", command=delete_passcode)
delete_button.pack(pady=5)

# Button to update passcode
update_button = customtkinter.CTkButton(app, text="Update Passcode", command=update_passcode)
update_button.pack(pady=5)

# Button to get passcode by ID
get_button = customtkinter.CTkButton(app, text="Get Passcode by ID", command=get_passcode)
get_button.pack(pady=5)

# Button to get all passcodes
get_all_button = customtkinter.CTkButton(app, text="Get All Passcodes", command=get_all_passcodes)
get_all_button.pack(pady=5)

app.mainloop()