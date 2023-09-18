import tkinter as tk

bg_color = 'green'

root = tk.Tk()

root.title("Polish Weather")
root.geometry("400x300")
root.configure(bg='lightblue')
root.eval("tk::PlaceWindow . center")
button = tk.Button(root, text="Kliknij mnie")
button.pack()


root.mainloop()




