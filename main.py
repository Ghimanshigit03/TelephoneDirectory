# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:21:12 2023

@author: AMIT GARG
"""
import pandas as pd
def print_menu():
    print("1. Print Phone Numbers")
    print("2. Add a Phone Number")
    print("3. Remove a Phone Number")
    print("4. Search a Phone Number")
    print("5. Modify a Phone Number")
    print("6. Quit")
    print()
df=pd.read_csv(r"C:\Users\AMIT GARG\OneDrive\Desktop\Telephone directory\data.csv",dtype={"Telephone Number": str})
print_menu()
print()
p=int(input("Enter choice from 1-6 - "))
print()
if (p==6):
    print("Quit")
while (p!=6):
    if(p==1):
        pd.set_option("display.max_columns", None) 
        pd.set_option("display.expand_frame_repr", False)
        print(df)
    if (p==2):
        telephone = input("Enter telephone number - ")
        name = input("Enter name - ")
        house_no = input("Enter house number - ")
        society_name = input("Enter name of the society - ")
        city = input("Enter name of city - ")
        pincode = input("Enter pincode of local area - ")
        state = input("Enter state - ")
        country = input("Enter country - ")
        new_data = {'Telephone Number' : telephone, 'Name' : name, 'House Number' : house_no,
                    'Society Name' : society_name, 'City' : city, 'Pin Code' : pincode,
                    'State' : state, 'Country' : country}
        
        new_row = pd.Series(new_data)
        new_row = pd.Series(new_data, name='Row')
        df = df.append(new_row, ignore_index=True)
        df.to_csv(r"C:\Users\AMIT GARG\OneDrive\Desktop\Telephone directory\data.csv", index=False)
        print("Data has been added successfully")
    if (p==3):
        telephone = input("Enter the telephone number to delete: ") 
        search_results = df.loc[df['Telephone Number'] == telephone] 
        if not search_results.empty: 
            df = df.drop(search_results.index) 
            print("Number deleted successfully") 
        else: 
            print("Number not found in the directory") 
        df.to_csv(r"C:\Users\AMIT GARG\OneDrive\Desktop\Telephone directory\data.csv", index=True)
    if (p==4):
        pd.set_option('display.max_columns', None) 
        pd.set_option('display.expand_frame_repr', False)
        print("How do you want to search the data?") 
        print("1 - Search using telephone number") 
        print("2 - Search using name") 
        print("3 - Search using address") 
        choice = int(input("Enter your choice: ")) 
        if choice == 1:
            search_info = 'telephone'  
            search_query = input("Enter the telephone number to search: ") 
            search_results = df.loc[df['Telephone Number'] == search_query]
        elif choice == 2:
            print("How do you want to search?")
            print("1 - Search by full name")
            print("2 - Search by first name")
            print("3 - Search by second name") 
            search_choice = int(input("Enter your choice: ")) 
            if search_choice == 1:
                search_info = 'Full Name'
                search_query = input("Enter the full name to search: ")
                search_results = df.loc[df['Name'] == search_query] 
            elif search_choice == 2:
                search_info = 'First Name'
                first_name = input("Enter the first name to search: ")
                search_results = df[df['Name'].str.startswith(first_name + ' ')]
            elif search_choice == 3:
                search_info = 'Second Name'
                second_name = input("Enter the second name to search: ")
                search_results = df[df['Name'].str.endswith(' ' + second_name)]
            else:
                print("Invalid choice.")
                search_results = pd.DataFrame()
        elif choice == 3:
            print("How do you want to search by address?")
            print("1 - Search by house number")
            print("2 - Search by society name")
            print("3 - Search by city")
            print("4 - Search by pin code")
            print("5 - Search by state")
            print("6 - Search by country") 
            address_choice = int(input("Enter your choice: ")) 
            if address_choice == 1:
                search_info = 'House Number'
                search_query = input("Enter the house number to search: ")
                search_results = df.loc[df['House Number'] == search_query] 
            elif address_choice == 2:
                search_info = 'Society Name'
                search_query = input("Enter the society name to search: ")
                search_results = df.loc[df['Society Name'] == search_query] 
            elif address_choice == 3:
                search_info = 'City'
                search_query = input("Enter the city to search: ")
                search_results = df.loc[df['City'] == search_query] 
            elif address_choice == 4:
                search_info = 'Pin code'
                search_query = input("Enter the pin code to search: ")
                search_results = df.loc[df['Pin code'] == search_query] 
            elif address_choice == 5:
                search_info = 'State'
                search_query = input("Enter the state to search: ")
                search_results = df.loc[df['State'] == search_query] 
            elif address_choice == 6:
                search_info = 'Country'
                search_query = input("Enter the country to search: ")
                search_results = df.loc[df['Country'] == search_query] 
            else:
                print("Invalid choice.") 
                search_results = pd.DataFrame()
        else:
            print("Invalid choice.") 
            search_results = pd.DataFrame() 
        if not search_results.empty:
            print("Search results based on {}: ".format(search_info))
            print(search_results) 
        else: 
            print("No matching records found.")
    if (p==5):
        old_telephone = input("Enter the telephone number whose details have to be changed: ") 
        telephone = input("Enter telephone number: ") 
        name = input("Enter name: ") 
        house_no = input("Enter house number: ") 
        society_name = input("Enter name of the society: ") 
        city = input("Enter name of city: ") 
        pincode = input("Enter pincode of the local area: ") 
        state = input("Enter state: ") 
        country = input("Enter country: ") 
        mask = df['Telephone Number'] == old_telephone 
        df.loc[mask, 'Telephone Number'] = telephone 
        df.loc[mask, 'Name'] = name 
        df.loc[mask, 'House Number'] = house_no 
        df.loc[mask, 'Society Name'] = society_name 
        df.loc[mask, 'City'] = city 
        df.loc[mask, 'Pin Code'] = pincode 
        df.loc[mask, 'State'] = state 
        df.loc[mask, 'Country'] = country  
        df.to_csv(r"C:\Users\AMIT GARG\OneDrive\Desktop\Telephone directory\data.csv", index=False) 
        print("Data has been changed successfully")
    print()
    print_menu()
    p=int(input("Enter choice from 1-6 - "))
    print()
    
        
