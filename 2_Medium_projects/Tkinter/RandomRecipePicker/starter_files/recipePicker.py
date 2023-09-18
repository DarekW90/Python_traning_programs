import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet
import os


bg_color = "#3d6466"
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)

# Połączenie z nazwą pliku
ubuntu_font = os.path.join(current_directory, 'fonts/Ubuntu-Bold.ttf')
shanti_font = os.path.join(current_directory, 'fonts/Shanti-Regular.ttf')
database = os.path.join(current_directory, 'data/recipes.db')
img_photo = os.path.join(current_directory, "assets/RRecipe_logo.png")
logo_photo = os.path.join(current_directory, "assets/RRecipe_logo_bottom.png")

pyglet.font.add_file(ubuntu_font)
pyglet.font.add_file(shanti_font)

def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
def fetch_db():
    connection= sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    
    idx = random.randint(0,len(all_tables)-1)
    
    #fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()
    
    connection.close()
    return table_name, table_records

def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])
    #print(title)
    
    ingredients = []
    
    #ingredients
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " of " + name)
    
    return title, ingredients
    #print(ingredients)    
        
def load_frame1():
    clear_widget(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    
    # frame1 widgets

    logo_img = ImageTk.PhotoImage(file=img_photo)
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(
        frame1, 
        text="ready for your random recipe",
        bg=bg_color,
        fg="white",
        font=("Shanti", 14)
        ).pack()
         
    # button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("Ubuntu", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).pack(pady=20)
    
def load_frame2():
    clear_widget(frame1)
    frame2.tkraise()
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)
    
    logo_img = ImageTk.PhotoImage(file=logo_photo)
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)
    
    tk.Label(
        frame2, 
        text=title,
        bg=bg_color,
        fg="white",
        font=("Ubuntu", 20)
        ).pack(pady=25)
    
    for i in ingredients:
        tk.Label(
            frame2, 
            text=i,
            bg="#28393a",
            fg="white",
            font=("Shanti", 12)
            ).pack(fill="both")
        
    tk.Button(
        frame2,
        text="BACK",
        font=("Ubuntu", 18),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
        ).pack(pady=20)
    
# initiallize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

# root.eval("tk::PlaceWindow . center")
# x = root.winfo_screenwidth() // 2
# y = int(root.winfo_screenheight() * 0.1)
# root.geometry('500x600+' + str(x) + '+' + str(y))


frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root,  bg=bg_color)

for frame in (frame1,frame2):
    frame.grid(row=0,column=0, sticky="nesw")
    
load_frame1()




# run app
root.mainloop()