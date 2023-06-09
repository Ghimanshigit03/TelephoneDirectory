# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:08:21 2023

@author: AMIT GARG
"""
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser

background = "#06283D"
framebg = "#EDEDED"

root = Tk()
root.title("Telephone Directory")
root.geometry("1250x700+210+100")
root.config(bg=background)

Label(root,text="Email : ghimanshi2003@gmail.com", width=10, height=3,bg="#f0687c",anchor='e').pack(side=TOP,fill=X)
Label(root,text="TELEPHONE DIRECTORY", width=10, height=2,bg="#ffc0cb",font='arial 20 bold').pack(side=TOP,fill=X)

file_path = "C:/Users/AMIT GARG/OneDrive/Desktop/Telephone directory/data.csv"

def print_phone_numbers():
    try:
        df = pd.read_csv(file_path)
        phone_numbers = df['Telephone Number'].tolist()
        names = df['Name'].tolist()
        tree.delete(*tree.get_children())
        for i in range(len(phone_numbers)):
            tree.insert("", "end", values=(phone_numbers[i], names[i]))
    except FileNotFoundError:
        messagebox.showwarning("Warning", "Data file not found")
        
telephone_entry = None

def add_phone_number():
    global telephone_entry
    if telephone_entry is None:
        messagebox.showwarning("Warning", "Please open the Add Phone Number window")
        return
    telephone = telephone_entry.get()
    name = name_entry.get()
    house_no = house_no_entry.get()
    society_name = society_name_entry.get()
    city = city_entry.get()
    pincode = pincode_entry.get()
    state = state_entry.get()
    country = country_entry.get()

    new_data = {'Telephone Number': telephone, 'Name': name, 'House Number': house_no,
                'Society Name': society_name, 'City': city, 'Pin Code': pincode,
                'State': state, 'Country': country}

    try:
        df = pd.read_csv(file_path)
        df = df.append(new_data, ignore_index=True)
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Success", "Data has been added successfully")
        clear_entries()
        print_phone_numbers()
    except FileNotFoundError:
        messagebox.showwarning("Warning", "Data file not found")

def open_add_window():
    global telephone_entry, name_entry, house_no_entry, society_name_entry, city_entry, pincode_entry, state_entry, country_entry

    add_window = Toplevel(root)
    add_window.title("Add Phone Number")
    add_window.configure(bg=background)

    def save_phone_number():
        telephone = telephone_entry.get()
        name = name_entry.get()
        house_no = house_no_entry.get()
        society_name = society_name_entry.get()
        city = city_entry.get()
        pincode = pincode_entry.get()
        state = state_entry.get()
        country = country_entry.get()

        if not telephone.strip() or not name.strip() or not house_no.strip() or not society_name.strip() \
                or not city.strip() or not pincode.strip() or not state.strip() or not country.strip():
            messagebox.showerror("Error", "Please fill in all the details.")
            return

        new_data = {
            'Telephone Number': telephone,
            'Name': name,
            'House Number': house_no,
            'Society Name': society_name,
            'City': city,
            'Pin Code': pincode,
            'State': state,
            'Country': country
        }

        try:
            df = pd.read_csv(file_path)
            df = df.append(new_data, ignore_index=True)
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", "Data has been added successfully")
            add_window.destroy()
            clear_entries()
            print_phone_numbers()
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Data file not found")

    telephone_frame = Frame(add_window, bg="#c4aead", pady=10)
    telephone_frame.pack(fill=X)

    telephone_label = Label(telephone_frame, text="Telephone Number:", font=("Arial", 14), bg="#c4aead")
    telephone_label.pack(side=LEFT, padx=(10, 5))

    telephone_entry = Entry(telephone_frame, font=("Arial", 14), bg="white")
    telephone_entry.pack(side=LEFT, padx=(0, 10))

    name_frame = Frame(add_window, bg="#c4aead", pady=10)
    name_frame.pack(fill=X)

    name_label = Label(name_frame, text="Name:", font=("Arial", 14), bg="#c4aead")
    name_label.pack(side=LEFT, padx=(10, 5))

    name_entry = Entry(name_frame, font=("Arial", 14), bg="white")
    name_entry.pack(side=LEFT, padx=(0, 10))

    house_no_frame = Frame(add_window, bg="#c4aead", pady=10)
    house_no_frame.pack(fill=X)

    house_no_label = Label(house_no_frame, text="House Number:", font=("Arial", 14), bg="#c4aead")
    house_no_label.pack(side=LEFT, padx=(10, 5))

    house_no_entry = Entry(house_no_frame, font=("Arial", 14), bg="white")
    house_no_entry.pack(side=LEFT, padx=(0, 10))

    society_name_frame = Frame(add_window, bg="#c4aead", pady=10)
    society_name_frame.pack(fill=X)

    society_name_label = Label(society_name_frame, text="Society Name:", font=("Arial", 14), bg="#c4aead")
    society_name_label.pack(side=LEFT, padx=(10, 5))

    society_name_entry = Entry(society_name_frame, font=("Arial", 14), bg="white")
    society_name_entry.pack(side=LEFT, padx=(0, 10))

    city_frame = Frame(add_window, bg="#c4aead", pady=10)
    city_frame.pack(fill=X)

    city_label = Label(city_frame, text="City:", font=("Arial", 14), bg="#c4aead")
    city_label.pack(side=LEFT, padx=(10, 5))

    city_entry = Entry(city_frame, font=("Arial", 14), bg="white")
    city_entry.pack(side=LEFT, padx=(0, 10))

    pincode_frame = Frame(add_window, bg="#c4aead", pady=10)
    pincode_frame.pack(fill=X)

    pincode_label = Label(pincode_frame, text="Pin Code:", font=("Arial", 14), bg="#c4aead")
    pincode_label.pack(side=LEFT, padx=(10, 5))

    pincode_entry = Entry(pincode_frame, font=("Arial", 14), bg="white")
    pincode_entry.pack(side=LEFT, padx=(0, 10))

    state_frame = Frame(add_window, bg="#c4aead", pady=10)
    state_frame.pack(fill=X)

    state_label = Label(state_frame, text="State:", font=("Arial", 14), bg="#c4aead")
    state_label.pack(side=LEFT, padx=(10, 5))

    state_entry = Entry(state_frame, font=("Arial", 14), bg="white")
    state_entry.pack(side=LEFT, padx=(0, 10))

    country_frame = Frame(add_window, bg="#c4aead", pady=10)
    country_frame.pack(fill=X)

    country_label = Label(country_frame, text="Country:", font=("Arial", 14), bg="#c4aead")
    country_label.pack(side=LEFT, padx=(10, 5))

    country_entry = Entry(country_frame, font=("Arial", 14), bg="white")
    country_entry.pack(side=LEFT, padx=(0, 10))

    save_button = Button(add_window, text="Save", command=save_phone_number, font=("Arial", 14, "bold"),
                         bg="#e799a3", fg="black", activebackground="#1565c0", activeforeground="white", bd=10)
    save_button.pack(pady=20)

def remove_phone_number():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a phone number to remove")
    else:
        phone_number = tree.item(selected_item)['values'][0]
        try:
            df = pd.read_csv(file_path)
            df = df.loc[df['Telephone Number'] != phone_number]
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", "Number deleted successfully")
            print_phone_numbers()
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Data file not found")

def view_details():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a phone number to view details")
    else:
        phone_number = tree.item(selected_item)['values'][0]
        try:
            df = pd.read_csv(file_path)
            details = df.loc[df['Telephone Number'] == phone_number].to_string(index=False)
            messagebox.showinfo("Details", details)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Data file not found")

# Create the main frame
main_frame = Frame(root, bg=framebg)
main_frame.pack(pady=20)

# Create the Treeview widget
tree = Treeview(main_frame, columns=("Telephone Number", "Name"), show="headings")
tree.heading("Telephone Number", text="Telephone Number")
tree.heading("Name", text="Name")
tree.column("Telephone Number", width=150)
tree.column("Name", width=200)
tree.pack(padx=10, pady=10)

# Define button styles
button_frame = Frame(root, bg=background)
button_frame.pack(pady=20)

# Define button styles
add_button_style = {
    "font": ("Arial", 15, "bold"),
    "bg": "#c4aead",
    "fg": "black",
    "padx": 20,
    "pady": 10,
    "activebackground": "#1976d2",
    "activeforeground": "white",
    "bd": 10,  # No border
}

remove_button_style = {
    "font": ("Arial", 15, "bold"),
    "bg": "#e799a3",
    "fg": "black",
    "padx": 20,
    "pady": 10,
    "activebackground": "#d32f2f",
    "activeforeground": "white",
    "bd": 10,  # No border
}

details_button_style = {
    "font": ("Arial", 15, "bold"),
    "bg": "#c4aead",
    "fg": "black",
    "padx": 20,
    "pady": 10,
    "activebackground": "#388e3c",
    "activeforeground": "white",
    "bd": 10,  # No border
}

add_button = Button(button_frame, text="Add", command=open_add_window, **add_button_style)
add_button.grid(row=0, column=0, padx=20, pady=10)

remove_button = Button(button_frame, text="Remove", command=remove_phone_number, **remove_button_style)
remove_button.grid(row=0, column=1, padx=20, pady=10)

details_button = Button(button_frame, text="View Details", command=view_details, **details_button_style)
details_button.grid(row=0, column=2, padx=20, pady=10)

# Display the phone numbers initially
print_phone_numbers()

root.mainloop()
