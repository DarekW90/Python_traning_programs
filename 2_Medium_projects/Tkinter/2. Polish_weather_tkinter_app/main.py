import tkinter as tk
from tkinter import *
import requests
import os
from tkinter import ttk


bg_color = 'lightblue'

root = tk.Tk()

root.title("Polish Weather")
root.geometry("400x350")
root.configure(bg=bg_color)
root.eval("tk::PlaceWindow . center")


def show(*args):
    selected_item = option_var.get()
    for row in data:
        if selected_item == row[0]:
            temperature = float(row[2])
            label.config(text=f"City: {row[0]}\n\n"
                         f"Observation Time: {row[1]} (hour)\n"
                         f"Temperature: {row[2]} \u2103\n"
                         f"Wind Speed: {row[3]} km/h\n"
                         f"Rain: {row[4]} mm\n"
                         f"Pressure: {row[5]} hPa")
            if temperature > 10:
                label.configure(bg='lightgreen')
                root.configure(bg='lightgreen')
            else:
                label.configure(bg='white')
                root.configure(bg='white')


url = 'https://danepubliczne.imgw.pl/api/data/synop'
response = requests.get(url)

options = ["Select city closest to you"]
data = []

for row in response.json():
    city = row['stacja']
    observation_time = row['godzina_pomiaru']
    temperature = row['temperatura']
    wind_speed = row['predkosc_wiatru']
    rain = row['suma_opadu']
    pressure = row['cisnienie']

    options.append(city)
    data.append([
        city,
        observation_time,
        temperature,
        wind_speed,
        rain,
        pressure
    ])

clicked = StringVar()

# Create button, it will change label text
option_var = tk.StringVar(value=options[0])
option_menu = ttk.OptionMenu(
    root, option_var, *options)
option_menu.pack(pady=10)

start_button = tk.Button(
        
        text="What's the weather ?",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=show,
        ).pack(pady=10)

# Create Label
hello_msg = 'Hi!\nMy easy-to-use weather station will allow\nyou to quickly check the current weather\nconditions in Poland.\n\nThe application allows you to \ndownload in real time weather conditions\nfrom the official API of the IMGW website.'


label_frame = Frame(root, bg=bg_color, bd=2, relief=SOLID)
label_frame.pack()

label = Label(label_frame, bg=bg_color, text=hello_msg, font=("Arial", 12))
label.pack()


# label = Label(label_frame, text=" ")
# label.pack()

# Execute tkinter
root.mainloop()
