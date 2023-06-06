# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:08:21 2023

@author: AMIT GARG
"""
import pandas as pd
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from tkinter import filedialog

background = "#06283D"
framebg = "#EDEDED"

root = Tk()
root.title("Telephone Directory")
root.geometry("1250x700+210+100")
root.config(bg=background)

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

def add_phone_number():
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

def clear_entries():
    telephone_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    house_no_entry.delete(0, 'end')
    society_name_entry.delete(0, 'end')
    city_entry.delete(0, 'end')
    pincode_entry.delete(0, 'end')
    state_entry.delete(0, 'end')
    country_entry.delete(0, 'end')

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

# Create the button frame
button_frame = Frame(root, bg=background)
button_frame.pack(pady=20)

add_button = Button(button_frame, text="Add", command=add_phone_number)
add_button.grid(row=0, column=0, padx=10)

remove_button = Button(button_frame, text="Remove", command=remove_phone_number)
remove_button.grid(row=0, column=1, padx=10)

clear_button = Button(button_frame, text="Clear", command=clear_entries)
clear_button.grid(row=0, column=2, padx=10)

details_button = Button(button_frame, text="View Details", command=view_details)
details_button.grid(row=0, column=3, padx=10)

# Display the phone numbers initially
print_phone_numbers()

root.mainloop()
