import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import sql

# PostgreSQL connection function
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="registration_db", 
            user="postgres", 
            password="123456", 
            host="localhost", 
            port="5432"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Connection Error", f"Error connecting to database: {e}")
        return None

# Insert data into the database
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return
    
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        insert_query = sql.SQL("INSERT INTO users (username, password) VALUES (%s, %s)")
        cursor.execute(insert_query, (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Registration successful.")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

# Create the UI
root = tk.Tk()
root.title("Registration")

label_username = tk.Label(root, text="Username")
label_username.grid(row=0, column=0)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

label_password = tk.Label(root, text="Password")
label_password.grid(row=1, column=0)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=2, columnspan=2)

root.mainloop()
