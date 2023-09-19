import tkinter as tk
from tkinter import *
import requests
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
            label.config(text=f"City: {row[0]}\n"
                         f"Observation Time: {row[1]} (hour)\n"
                         f"Temperature: {row[2]} \u2103\n"
                         f"Wind Speed: {row[3]} km/h\n"
                         f"Rain: {row[4]} mm\n"
                         f"Pressure: {row[5]} hPa")
            if temperature > 10:
                label.configure(bg='green')
                root.configure(bg='green')
            else:
                root.configure(bg='white')
                label.configure(bg='white')


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
    root, option_var, *options, command=show)
option_menu.pack(padx=10, pady=10)

# Create Label
label = Label(root, background=bg_color, text=" ")
label.pack()

# Execute tkinter
root.mainloop()
