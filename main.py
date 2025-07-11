import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
import numpy as np
import warnings
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font
from PIL import Image, ImageTk
warnings.simplefilter(action='ignore', category=FutureWarning)

pd.set_option('future.no_silent_downcasting', True)   #There are many warnings shown due to some pandas functions, that's why i used this

# Loading data
house_dataset = pd.read_excel('processed_file_new.xlsx')

# Clean 'repair' column: replace empty strings or NaNs with 'no'
house_dataset['repair'].replace(r'^\s*$', 'yoxdur', regex=True, inplace=True) #Replaced empty strings or NaNs with 'no'
house_dataset['repair'].fillna('yoxdur', inplace=True)

house_dataset.replace({'repair': {'var': 1, 'yoxdur': 0}}, inplace=True)     # Replaced categorical strings with numerical codes for certain columns
house_dataset.replace({'title_deed': {'var': 1, 'yoxdur': 0}}, inplace=True)
house_dataset.replace({'category': {'yeni': 1, 'kohne': 0}}, inplace=True)

house_dataset['title_deed'] = house_dataset['title_deed'].astype(int)
house_dataset['repair'] = house_dataset['repair'].astype(int)

house_dataset['area'] = house_dataset['area'].str.replace('m²', '', regex=False).str.replace(' ', '').str.split('.').str[0].astype(int) #Cleaned numeric columns
house_dataset['price'] = house_dataset['price'].str.replace(' ', '').astype(int)
house_dataset['room_number'] = house_dataset['room_number'].astype(int)

house_dataset.drop(columns=['currency', 'title', 'address', 'region'], inplace=True)
house_dataset.drop('price_1m2', axis=1, inplace=True)
#house_dataset.info()
house_dataset = house_dataset[~house_dataset['region_new'].isin(['Pirallahi', 'Qaradag'])]

house_dataset = pd.get_dummies(house_dataset, columns=['region_new'], prefix='region').astype(int)

X = house_dataset.drop(columns=['price'])
y = house_dataset['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
train_data = X_train.join(y_train)

X_train, y_train = train_data.drop(['price'], axis=1), train_data['price']
test_data = X_train.join(y_train)

forest = RandomForestRegressor()
forest.fit(X_train, y_train)



columns = X_train.columns

root = tk.Tk()
root.title("AZE")
root.geometry("800x500")
root.iconbitmap("favicon.ico")

bg_image = Image.open("baku_image.png")  
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(root, text="Baku House Price Prediction Project", font=("Helvetica", 24, "bold"))
title_label.pack(pady=10)

user_data = {}
big_font = font.Font(size=18)
area_label = tk.Label(root, text="Enter the area(m2):", font=("Helvetica", 16, "bold"))
area_label.pack(pady=15)
area_entry = tk.Entry(root, justify='right', width=15, font=big_font)
area_entry.pack()


def area_next():
    val = area_entry.get()
    if val.isdigit():
        if int(val)>20 and int(val) < 300:
            user_data['area'] = int(val)
            area_label.pack_forget()
            area_entry.pack_forget()
            area_next_btn.pack_forget()
            ask_room_number()
        else:
            area_label.config(text="❌ The area must be within 20-300(m2)")
    else:
        area_label.config(text="❌ Please enter a valid number for area")

area_next_btn = tk.Button(root, text="Next", command=area_next)
area_next_btn.pack(pady=10)

#Widgets
room_label = tk.Label(root, text="Enter number of rooms:", font=("Helvetica", 16, "bold"), bg="white")
room_entry = tk.Entry(root, justify='right', width=15, font=big_font)
room_next_btn = tk.Button(root, text="Next")

def room_next():
    val = room_entry.get()
    if val.isdigit():
        if int(val)>0 and int(val) < 10:
            user_data['room_number'] = int(val)
            room_label.pack_forget()
            room_entry.pack_forget()
            room_next_btn.pack_forget()
            ask_title_deed()
        else:
            room_label.config(text="❌ The room must be within 1-10")
    else:
        room_label.config(text="❌ Please enter a valid number for rooms")

room_next_btn.config(command=room_next)

def ask_room_number():
    room_label.pack(pady=15)
    room_entry.pack()
    room_next_btn.pack(pady=10)

#Title Deed with Yes/No buttons
def ask_title_deed():
    label = tk.Label(root, text="Does it have a title deed?", font=("Helvetica", 16, "bold"), bg="white")
    label.pack(pady=15)

    def select_yes():
        user_data['title_deed'] = 1
        label.pack_forget()
        yes_btn.pack_forget()
        no_btn.pack_forget()
        ask_repair()

    def select_no():
        user_data['title_deed'] = 0
        label.pack_forget()
        yes_btn.pack_forget()
        no_btn.pack_forget()
        ask_repair()

    yes_btn = tk.Button(root, text="Yes", font=big_font, width=8, command=select_yes)
    yes_btn.pack(pady=5)

    no_btn = tk.Button(root, text="No", font=big_font, width=8, command=select_no)
    no_btn.pack()

#Repair with Yes/No buttons
def ask_repair():
    label = tk.Label(root, text="Is it repaired?", font=("Helvetica", 16, "bold"), bg="white")
    label.pack(pady=15)

    def select_yes():
        user_data['repair'] = 1
        label.pack_forget()
        yes_btn.pack_forget()
        no_btn.pack_forget()
        ask_category()

    def select_no():
        user_data['repair'] = 0
        label.pack_forget()
        yes_btn.pack_forget()
        no_btn.pack_forget()
        ask_category()

    yes_btn = tk.Button(root, text="Yes", font=big_font, width=8, command=select_yes)
    yes_btn.pack(pady=5)

    no_btn = tk.Button(root, text="No", font=big_font, width=8, command=select_no)
    no_btn.pack()

#Category with Yes/No buttons
def ask_category():
    label = tk.Label(root, text="Is it new?", font=("Helvetica", 16, "bold"), bg="white")
    label.pack(pady=15)

    def select_yes():
        user_data['category'] = 1  # yeni
        label.pack_forget()
        yes_btn.pack_forget()
        no_btn.pack_forget()
        ask_region()

    def select_no():
        user_data['category'] = 0  # kohne
        label.pack_forget()
        yes_btn.pack_forget()
        no_btn.pack_forget()
        ask_region()

    yes_btn = tk.Button(root, text="Yes", font=big_font, width=8, command=select_yes)
    yes_btn.pack(pady=5)

    no_btn = tk.Button(root, text="No", font=big_font, width=8, command=select_no)
    no_btn.pack()

def ask_region():
    label = tk.Label(root, text="Select the region:", font=("Helvetica", 16, "bold"), bg="white")
    label.pack(pady=15)
    region_list = [
        "Nizami", "Yasamal", "Nerimanov", "Bineqedi", "Khatai",
        "Sabail", "Surakhani", "Nasimi", "Garadagh", "Sabunchu"
    ]

    buttons = []

    def select_region(region_name):
        user_data['region'] = region_name
        label.pack_forget()
        for btn in buttons:
            btn.pack_forget()
        run_prediction()


    for region in region_list:
        btn = tk.Button(root, text=region, font=("Helvetica", 12), width=15,
                        command=lambda r=region: select_region(r))
        btn.pack(pady=2)
        buttons.append(btn)


def run_prediction():
    input_data = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)
    input_data.at[0, 'area'] = user_data['area']
    input_data.at[0, 'room_number'] = user_data['room_number']
    input_data.at[0, 'repair'] = user_data['repair']
    input_data.at[0, 'title_deed'] = user_data['title_deed']
    input_data.at[0, 'category'] = user_data['category']

    region_col = f"region_{user_data['region']}"
    if region_col in input_data.columns:
        input_data.at[0, region_col] = 1
    else:
        messagebox.showerror("Error", f"❌ Region '{user_data['region']}' not found in model.")
        return

    predicted_price = forest.predict(input_data)[0]
    messagebox.showinfo("Predicted Price", f"💰 Estimated Price: {int(predicted_price):,} AZN")

root.mainloop()
